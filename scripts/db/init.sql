-- Wedding Dress Database Initialization
-- Create necessary tables for the wedding dress recommendation system

-- Table: wedding_dresses
CREATE TABLE IF NOT EXISTS wedding_dresses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2),
    style VARCHAR(100),
    size VARCHAR(50),
    color VARCHAR(50),
    fabric VARCHAR(100),
    availability BOOLEAN DEFAULT TRUE,
    image_url VARCHAR(500),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_style (style),
    INDEX idx_availability (availability)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table: surveys
-- Stores anonymous body measurement surveys and dress recommendations
CREATE TABLE IF NOT EXISTS surveys (
    id INT AUTO_INCREMENT PRIMARY KEY,

    -- Body measurements (survey inputs)
    arm_length ENUM('short', 'medium', 'long') NOT NULL,
    leg_length ENUM('short', 'medium', 'long') NOT NULL,
    neck_length ENUM('short', 'medium', 'long') NOT NULL,
    face_shape ENUM('oval', 'wide', 'angular', 'long') NOT NULL,
    body_type ENUM('thin', 'medium', 'heavy') NOT NULL,

    -- Recommended dress
    dress_id INT,

    -- Event information
    event_date DATE,
    notes TEXT,

    -- Metadata
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    -- Foreign keys and indexes
    FOREIGN KEY (dress_id) REFERENCES wedding_dresses(id) ON DELETE SET NULL,
    INDEX idx_body_type (arm_length, leg_length, neck_length, face_shape, body_type),
    INDEX idx_dress (dress_id),
    INDEX idx_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Sample data for wedding_dresses
INSERT INTO wedding_dresses (name, description, price, style, size, color, fabric) VALUES
('Classic A-Line Gown', 'Elegant A-line wedding dress with lace details', 1299.99, 'A-Line', 'M', 'White', 'Lace'),
('Modern Mermaid Dress', 'Sophisticated mermaid style with train', 1599.99, 'Mermaid', 'S', 'Ivory', 'Satin'),
('Vintage Ball Gown', 'Romantic ball gown with tulle layers', 1899.99, 'Ball Gown', 'L', 'White', 'Tulle');
