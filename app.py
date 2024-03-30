import streamlit as st


st.title("Matthew Zhang's Website")

titles = ["About", "Education", "Work Experience", "Hobbies and Interests", "Interest Projects"]

tabs = st.tabs(titles)

texts = ['''
### I am Matthew Zhang, and welcome to my website!
''',
'''
| Start Date | End Date | School | Degree |
|----------|----------|----------|----------|
| 2023 | 2025 | University of Washington | Master of Science in Technology Innovation, Robotics |
| 2022 | 2025 | Tsinghua University | Master of Science in Data Science and Information Technology |
| 2018 | 2022 | Tsinghua University | Bachelor of Engineering in Computer Science and Technology |
''', 
'''
I don't have any full-time work experience before, but my interests lie in the intersection of Machine Learning, Quantitative Trading and Research and Human Computer Interaction. Feel free to connect with me through [Linkedin](https://www.linkedin.com/in/matthew-zhang05/). 
''', 
'''
- Basketball
- Photography
- Bodybuilding
''',
'''
Check out my interesting research projects through my [Google Scholar](https://scholar.google.com/citations?user=l2gfgmEAAAAJ&hl=en)
''']

for i, tab in enumerate(tabs):
    with tab:
        # st.header(titles[i])
        if i == 0:
            st.image('images/selfie.webp', width=400)
        st.markdown(texts[i])
        
