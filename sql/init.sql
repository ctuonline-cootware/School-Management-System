-- Create development role
CREATE ROLE dev_user WITH LOGIN PASSWORD 'cs491';

-- Create application role
CREATE ROLE app_user WITH LOGIN PASSWORD 'cs491';

-- Create the main database
CREATE DATABASE school_management OWNER dev_user;

-- Grant privileges to dev_user
GRANT ALL PRIVILEGES ON DATABASE school_management TO dev_user;
