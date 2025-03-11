# Reference
<details><summary><code>client.<a href="src/amniscient/client.py">load_model</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initializes a model for inference. This endpoint must be called before running any detections.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from amniscient import AmniscientApi

client = AmniscientApi(
    api_key="YOUR_API_KEY",
)
client.load_model(
    model_id="model_id",
    organization_id="organization_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**model_id:** `str` — The model ID of an active and trained AI model within your organization
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `str` — Your organization identifier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

