CREATE TABLE device (
    id             SERIAL PRIMARY KEY,
    device_key     CHAR(36) NOT NULL,
    signature_key  VARCHAR(255) NOT NULL,
    name           VARCHAR(255) NOT NULL,
    settings       JSONB NOT NULL,
    created_at     TIMESTAMP NOT NULL DEFAULT NOW(),
    deactivated_on TIMESTAMP,
    unique(device_key)
);
