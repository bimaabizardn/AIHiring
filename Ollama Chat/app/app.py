import os
import streamlit as st
import ollama

# --- Pastikan host diarahkan ke port default ---
os.environ["OLLAMA_HOST"] = "http://127.0.0.1:11434"

# --- Setup halaman ---
st.set_page_config(page_title="Gemma3:1b Chat", page_icon="🤖")
st.title("🤖 Gemma3:1b Chat")

# --- Inisialisasi client Ollama ---
try:
    client = ollama.Client(host="http://127.0.0.1:11434")
    st.session_state.ollama_client_status = "connected"
except Exception as e:
    st.session_state.ollama_client_status = "failed"
    st.error("❌ Gagal terhubung ke Ollama. Pastikan Ollama server sedang berjalan.")
    st.stop()

# --- Inisialisasi riwayat chat ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Tampilkan riwayat chat sebelumnya ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Input chat ---
if prompt := st.chat_input("Apa pertanyaan Anda?"):
    # Tambahkan pesan user ke riwayat
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Tampilkan pesan user
    with st.chat_message("user"):
        st.markdown(prompt)

    # Jawaban dari model
    if st.session_state.ollama_client_status == "connected":
        with st.chat_message("assistant"):
            with st.spinner("🤖 Gemma3:1b sedang berpikir..."):
                try:
                    # Kirim riwayat percakapan ke model
                    response = client.chat(
                        model="gemma3:1b",
                        messages=[
                            {"role": m["role"], "content": m["content"]}
                            for m in st.session_state.messages
                        ]
                    )

                    # Ambil jawaban
                    ai_message = response["message"]["content"]

                    # Tampilkan jawaban
                    st.markdown(ai_message)

                    # Simpan ke riwayat chat
                    st.session_state.messages.append(
                        {"role": "assistant", "content": ai_message}
                    )

                except ollama.ResponseError as e:
                    st.error("❌ Gagal memanggil model. Pastikan 'gemma3:1b' sudah diunduh.")
                    st.write(f"Detail error: {e}")
                except Exception as e:
                    st.error("⚠️ Terjadi kesalahan saat berkomunikasi dengan model.")
                    st.write(f"Detail error: {e}")
    else:
        with st.chat_message("assistant"):
            st.markdown("❌ Tidak dapat terhubung ke server Ollama. Periksa instalasi Anda.")
