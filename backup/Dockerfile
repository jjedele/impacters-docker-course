# 1. Start from a fitting base layer
FROM python

# 2. Copy required files into the image
WORKDIR /app
COPY app.py ./
COPY requirements.txt ./

# 3. Install Python requirements
RUN pip3 install -r requirements.txt

# 4. Setup Container entrypoint
ENTRYPOINT [ "python3", "app.py" ]
CMD [ "print_config" ]

# 5. Expose HTTP port
EXPOSE 8000

# 6. (Optional) Set default configs
ENV GREETING="Hello World"


# Build with: docker build -t app:v1 .
