package com.example;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.springframework.web.bind.annotation.*;

import java.net.URLDecoder;
import java.nio.charset.StandardCharsets;

@RestController
public class LogController {
    private static final Logger logger = LogManager.getLogger(LogController.class);

    @PostMapping("/log")
    public String logInput(@RequestParam String input) {
        // Decode user input **before** checking for exploits
        String decodedInput = URLDecoder.decode(input, StandardCharsets.UTF_8);

        // Block Log4Shell exploit attempts BEFORE logging
        if (decodedInput.matches(".*\\$\\{.*jndi:.*}.*")) {
            return "Invalid input detected";
        }

        // Log the sanitized input
        logger.info("User input: " + decodedInput);

        return "Logged: " + decodedInput;
    }
}
