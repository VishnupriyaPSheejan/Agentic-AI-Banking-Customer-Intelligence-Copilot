FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python src/generate_data.py && python src/build_index.py
EXPOSE 8501
CMD ["streamlit","run","src/app.py","--server.address=0.0.0.0","--server.port=8501"]
