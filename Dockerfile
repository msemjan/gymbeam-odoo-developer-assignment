FROM odoo:16

# Copy requirements.txt into container
COPY requirements.txt /tmp/requirements.txt

# Install additional Python libraries
RUN python3 -m pip install --no-cache-dir -r /tmp/requirements.txt
