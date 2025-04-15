FROM python:3.13-slim

# Create and activate virtual environment
RUN python3 -m venv /venv

# Add venv to PATH
ENV PATH="/venv/bin:$PATH"

# Install Django inside the venv
RUN pip install --upgrade pip && pip install "django<6"

# Copy project source code
COPY src /src
WORKDIR /src

# Expose the default Django dev server port
EXPOSE 8888

# Run the server
RUN python manage.py migrate --noinput
CMD python manage.py runserver 0.0.0.0:8888
