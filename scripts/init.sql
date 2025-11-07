-- Wedding Dress Recommendation Database Schema

CREATE DATABASE IF NOT EXISTS wedding_dress_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE wedding_dress_db;

-- Recommendation queries table
CREATE TABLE IF NOT EXISTS recommendation_queries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    query_hash VARCHAR(64) UNIQUE NOT NULL,

    -- Input parameters
    arm_length VARCHAR(20) NOT NULL,
    leg_length VARCHAR(20) NOT NULL,
    neck_length VARCHAR(20) NOT NULL,
    face_shape VARCHAR(20) NOT NULL,
    body_type VARCHAR(20) NOT NULL,

    -- Result (JSON)
    recommendation JSON NOT NULL,

    -- Metadata
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    access_count INT DEFAULT 0,
    last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    -- Indexes
    INDEX idx_query_hash (query_hash),
    INDEX idx_created_at (created_at),
    INDEX idx_query_params (arm_length, leg_length, neck_length, face_shape, body_type),
    INDEX idx_access_count (access_count)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Event log table for analytics
CREATE TABLE IF NOT EXISTS event_logs (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    event_type VARCHAR(50) NOT NULL,
    query_hash VARCHAR(64),
    user_id VARCHAR(100),
    metadata JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    INDEX idx_event_type (event_type),
    INDEX idx_created_at (created_at),
    INDEX idx_query_hash (query_hash),
    FOREIGN KEY (query_hash) REFERENCES recommendation_queries(query_hash)
        ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
