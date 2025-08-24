import os
import json
import streamlit as st

st.set_page_config(
    page_title="AI Shopping Assistant",
    page_icon="🛍",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ---------------- Sidebar: Settings ----------------
st.sidebar.header("⚙ Settings")

default_key = os.getenv("GOOGLE_API_KEY", "")
api_key = st.sidebar.text_input(
    "Gemini API key",
    value=default_key,
    type="password",
    placeholder="Paste your Google Gemini API key"
)

model_name = st.sidebar.selectbox("Model", ["gemini-1.5-flash", "gemini-1.5-pro"], index=0)

# ---------------- Main UI ----------------
st.title("🛍 AI Virtual Shopping Assistant")
st.caption("Describe what you want — budget, style, category — and get smart picks.")

# ------- Demo catalog with images (12 items) -------
CATALOG = [
    # Clothing
    {"name": "Blue T-Shirt", "category": "Clothing", "price": 20, "style": "Casual",
     "image": "https://images.unsplash.com/photo-1512436991641-6745cdb1723f?auto=format&w=800&q=80"},
    {"name": "Slim-Fit Chinos", "category": "Clothing", "price": 32, "style": "Smart Casual",
     "image": "https://images.unsplash.com/photo-1520974735194-6a4f4bafab63?auto=format&w=800&q=80"},
    {"name": "Denim Jacket", "category": "Clothing", "price": 45, "style": "Casual",
     "image": "https://images.unsplash.com/photo-1503342452485-86ff0a8bccc5?auto=format&w=800&q=80"},
    {"name": "Athletic Hoodie", "category": "Clothing", "price": 28, "style": "Athleisure",
     "image": "https://images.unsplash.com/photo-1544441893-675973e31985?auto=format&w=800&q=80"},

    # Footwear
    {"name": "Running Sneakers", "category": "Footwear", "price": 35, "style": "Athleisure",
     "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&w=800&q=80"},
    {"name": "Formal Black Shoes", "category": "Footwear", "price": 50, "style": "Formal",
     "image": "https://images.unsplash.com/photo-1520256862855-398228c41684?auto=format&w=800&q=80"},
    {"name": "Slip-on Canvas", "category": "Footwear", "price": 22, "style": "Casual",
     "image": "https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&w=800&q=80"},

    # Electronics
    {"name": "Wireless Headphones", "category": "Electronics", "price": 80, "style": "Modern",
     "image": "https://images.unsplash.com/photo-1518443870897-85f15fd4d5d0?auto=format&w=800&q=80"},
    {"name": "Smartwatch", "category": "Electronics", "price": 60, "style": "Minimal",
     "image": "https://images.unsplash.com/photo-1518441902119-8897f33d0e3e?auto=format&w=800&q=80"},

    # Accessories
    {"name": "Leather Belt", "category": "Accessories", "price": 18, "style": "Classic",
     "image": "https://images.unsplash.com/photo-1601121141461-9d5b2e3e7893?auto=format&w=800&q=80"},
    {"name": "Wayfarer Sunglasses", "category": "Accessories", "price": 25, "style": "Casual",
     "image": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&w=800&q=80"},

    # Home & Kitchen
    {"name": "Insulated Water Bottle", "category": "Home & Kitchen", "price": 15, "style": "Everyday",
     "image": "https://images.unsplash.com/photo-1607346256330-dee7af15f7d0?auto=format&w=800&q=80"},
]

# --------- Filters ---------
col1, col2 = st.columns(2)
with col1:
    budget = st.number_input("Max Budget ($)", min_value=1, value=50)
with col2:
    categories = st.multiselect(
        "Categories",
        sorted({p["category"] for p in CATALOG}),
        default=[]
    )

need = st.text_input(
    "Tell me what you’re looking for",
    placeholder="e.g., casual shoes under $40 for daily use"
)

# --------- Helpers ---------
def render_cards(products, title="Results"):
    if not products:
        st.info("No products matched your filters.")
        return
    st.markdown(f"### {title}")
    cols = st.columns(3)
    for i, p in enumerate(products):
        with cols[i % 3]:
            st.image(p["image"], use_container_width=True)
            st.markdown(f"**{p['name']}**")
            st.caption(f"{p['category']} • {p['style']}")
            st.write(f"${p['price']}")

# --------- Action ---------
if st.button("Find Products"):
    # 1) Filter by budget + category
    filtered = [
        p for p in CATALOG
        if p["price"] <= budget and (not categories or p["category"] in categories)
    ]
    render_cards(filtered, title="Matching Products")

    # 2) LLM recommendations (optional, only if key present)
    if not api_key.strip():
        st.warning("Please provide your Gemini API key in the sidebar for AI recommendations.")
    else:
        try:
            # Lazy import so UI doesn't crash if package missing
            import google.generativeai as genai
            genai.configure(api_key=api_key.strip())
            model = genai.GenerativeModel(model_name)

            prompt = f"""
You are a shopping assistant. From this product list, pick the best matches:
{json.dumps(filtered, ensure_ascii=False)}

User need: {need}

Return a short, bulleted recommendation list. For each pick, include:
- Why it matches the user's need
- Price and category
- Any style notes
Keep it under 120 words.
"""
            resp = model.generate_content(prompt)
            st.markdown("### 🎯 AI Recommendations")
            st.write(resp.text)
        except ModuleNotFoundError:
            st.error("Package `google-generativeai` not installed. Run: `pip install google-generativeai`")
        except Exception as e:
            st.error(f"Error generating recommendations: {e}")

st.write("---")
st.caption("Demo catalog used. Replace with Shopify or a live API for production.")
