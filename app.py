#import libraries
import requests
import streamlit as st
import streamlit_lottie as stl

#set page config
st.set_page_config(page_title="Chep's Place", page_icon=":tada:", layout="wide")

#load lottie url
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/styles.css")

#load assets
lottie_coding = load_lottieurl("https://lottie.host/36a2ea3b-8cf6-4346-b687-59f58b42e8ea/mEn0IFXk5n.json")
lottie_coding_two = load_lottieurl("https://lottie.host/c0f7fb70-59f7-423a-9230-c177c6fa5d58/tVYUSIktUx.json")

#header section
with st.container():
    st.write("##")
    st.header("Most people call me Chep :boom: :rocket:")
    st.title("I'm A Developer, Father, & Bitcoiner based in Boston")
    st.write("I have a passion for leveraging open-source technologies that enable peer-to-peer value transfers. My goal is to help others see why value for value is so important. One day I'd like to see an internet subsidized by its users rather than ads. Creators are starting to directly engage their audience for support, which means not having to rely on corporate sponsors. I also believe in the power of compounding so I've committed to writing daily, for life or until Medium goes out of business.")
    st.markdown("[My Medium](https://medium.com/@chepenikconor)")

#About me
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Youtube")
        st.write("##")
        st.write(
                        """
I created this channel to share tips, insights, and occasional humor to help individuals leverage open source tools, grow personally, and succeed. Content includes
- Engaging article reads and thoughtful commentary. 
- Podcasts focused on developing positive habits and harnessing the power of compounding for long-term success.
- Lessons on web development.

If you crave practical and entertaining videos covering technology, finance, and personal growth, subscribe to my channel! Likes and comments are appreciated, as they aid the algorithm in sharing my content with a wider audience. 
"""
        )
    with right_column:
        stl.st_lottie(lottie_coding, height=500, key="coding")

#myservices
with st.container():
    st.write("---")
    st.header("My Web Development Services")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("images/30mincall.png", width=200)
        st.image("images/personalSite.png", width=200)
    with text_column:
        st.subheader("30 min call or a customized personal website built")
        st.write(
            """
                - For 21 USD worth of sats 30 minutes of my time is yours. We can chat about Bitcoin, tech, or just crack some jokes!
                - For 100 USD worth of sats I will build you a customized personal website. 
                - Use the contact form below to send me a screenshot of your magicwebstore receipt plus some times that work for you.
            """
        )
        st.markdown("[Chep's Magic Webstore Link](https://magicwebstore.xyz/index.html?pubkey=02b1a6c208420d3eb5a625aa8c79689e1dd4ea94f82286d06e1df7a05e2c3a482f&relays=%5B%22wss://nostrue.com%22,%22wss://relayable.org%22,%22wss://nostr.oxtr.dev%22%5D)")


#contact
with st.container():
    st.write("---")
    st.header("Get in touch with me :)")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/eab4c130f00412b3d328a87920ac3ad3" method="POST" />
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        stl.st_lottie(lottie_coding_two, height=369, key="notcoding")