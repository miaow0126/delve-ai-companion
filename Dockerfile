FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir "mcp[cli]" uvicorn
ENV DELVE_HTTP=8900
EXPOSE 8900
CMD ["python", "delve_mcp.py"]
