import streamlit as st
import os

# بيعرف مكان الفولدر اللي فيه الملف حالياً أوتوماتيك
base_path = os.path.dirname(os.path.abspath(__file__))

# إعدادات الصفحة
st.set_page_config(page_title="شركة السهم للدعاية والإعلان", page_icon="🎯", layout="wide")

# القائمة الجانبية
with st.sidebar:
    logo_path = os.path.join(base_path, "logo.png")
    if os.path.exists(logo_path):
        st.image(logo_path, use_container_width=True)
    else:
        st.title("🏹 شركة السهم")
    
    st.markdown("---")
    choice = st.radio("انتقل إلى:", ["الرئيسية", "سابقة أعمالنا", "تواصل معنا"])

# صفحة الرئيسية
if choice == "الرئيسية":
    st.markdown("<h1 style='text-align: center; color: #1e3a8a;'>شركة السهم للدعاية والإعلان</h1>", unsafe_allow_html=True)
    factory_path = os.path.join(base_path, "factory.jpg")
    if os.path.exists(factory_path):
        st.image(factory_path, use_container_width=True)
    else:
        st.warning("⚠️ صورة الواجهة (factory.jpg) غير موجودة في الفولدر.")

# صفحة سابقة الأعمال
elif choice == "سابقة أعمالنا":
    st.header("📸 معرض أعمالنا")
    cols = st.columns(3)
    for i in range(1, 13):
        with cols[(i-1) % 3]:
            img_name = f"stile{i}.jpg"
            full_img_path = os.path.join(base_path, img_name)
            if os.path.exists(full_img_path):
                st.image(full_img_path, caption=f"عمل رقم {i}", use_container_width=True)
            else:
                st.write(f"🖼️ صورة {i} مفقودة")

# صفحة التواصل
elif choice == "تواصل معنا":
    st.header("📞 تواصل معنا")
    st.info("📍 العنوان: المكتب الرئيسي - الدقي")
    st.success("📱 مبيعات: 0123456789")