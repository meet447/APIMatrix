#Manga

| Name      | Website       | type  | Status  |
|-----------|---------------|-------|---------|
| comick    | comick.cc     | manga | working | 
|           |               |       |         | 
|           |               |       |         |  

### 1. Get Bing Text Genration

- **Endpoint:** `/api/llm/gpt4/bing/<message>`

#### Example Code

```python
import requests

message = "hello!"

url = f"https://apimatrix.vercel.app/api/llm/bing/{message}"
response = requests.get(url)
result = response.json()
print(result)
```

#### Response Format

```json
{"response":""}
```