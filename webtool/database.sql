DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS components;
DROP TABLE IF EXISTS product_component;

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    description TEXT NOT NULL,
    sku INT NOT NULL
);

CREATE TABLE product_component (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    FOREIGN KEY (product_id) REFERENCES products (id),
    FOREIGN KEY (component_id) REFERENCES components (id), 
);

CREATE TABLE components (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    description TEXT NOT NULL,
    irritating BOOL NOT NULL
);