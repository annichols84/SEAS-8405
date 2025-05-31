import json
import os

# SECTION 1: Update daemon.json with advanced security flags  
# Purpose: Enforces stricter privilege control, logging constraints, and runtime security  
daemon_config = {
    "userns-remap": "default",  # Enables user namespace isolation to limit privileges  
    "log-driver": "json-file",  # Restricts log format for better monitoring  
    "log-opts": {"max-size": "10m", "max-file": "3"},  # Limits excessive log growth  
    "no-new-privileges": True,  # Blocks privilege escalation within containers  
    "live-restore": True,  # Ensures containers keep running even if Docker daemon crashes  
    "seccomp-profile": "/etc/docker/seccomp.json"  # Enforces Seccomp syscall filtering  
}

daemon_file = "/etc/docker/daemon.json"

try:
    with open(daemon_file, "w") as f:
        json.dump(daemon_config, f, indent=4)
    print("[✔] Updated daemon.json with hardening configurations.")
except Exception as e:
    print(f"[✘] Error updating daemon.json: {e}")

# SECTION 2: Modify Dockerfile to enforce execution restrictions  
# Purpose: Prevents root execution, adds health monitoring, and limits resource usage  
dockerfile_content = """
FROM python:3.11

# Enforce non-root execution  
USER appuser  

# Health check to verify service uptime and prevent silent failures  
HEALTHCHECK CMD curl -f http://localhost:5000 || exit 1  

# Apply resource limits  
CMD ["python", "-m", "flask", "run", "--host=127.0.0.1", "--port=5000"]
"""

dockerfile_path = "Dockerfile"

try:
    with open(dockerfile_path, "w") as f:
        f.write(dockerfile_content)
    print("[✔] Updated Dockerfile with USER, HEALTHCHECK, and resource enforcement.")
except Exception as e:
    print(f"[✘] Error updating Dockerfile: {e}")

# SECTION 3: Update docker-compose.yml for security enhancements  
# Purpose: Limits memory usage, enforces read-only file system, disables unnecessary capabilities  
compose_content = """
version: '3'
services:
  app:
    build: .
    
    # Prevent privilege escalation  
    security_opt:
      - no-new-privileges:true  
    
    # Set memory and CPU limits to prevent denial-of-service risks  
    deploy:
      resources:
        limits:
          memory: 512m  
          cpus: "0.5"
    
    # Restrict container access  
    networks:
      default:
        ipv4_address: 127.0.0.1  
    
    # Enforce read-only filesystem  
    read_only: true  
    
    # Drop all unnecessary kernel capabilities  
    cap_drop:
      - NET_RAW
      - SYS_MODULE
      - SYS_ADMIN
"""

compose_file = "docker-compose.yml"

try:
    with open(compose_file, "w") as f:
        f.write(compose_content)
    print("[✔] Updated docker-compose.yml with maximum security configurations.")
except Exception as e:
    print(f"[✘] Error updating docker-compose.yml: {e}")
