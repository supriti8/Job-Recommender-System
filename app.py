from prediction import recommend_jobs
import streamlit as st


def predict_jobs(userid):
    response = recommend_jobs(userid)
    print(response)
    return response


def main():
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Job Recommendation Application</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    userid = st.slider('Slide to select User ID', min_value=1, max_value=671)
    result = " "
    if st.button("Recommend"):
        result = predict_jobs(userid=userid)
    st.success(f'The recommended jobs for user {userid} are:')
    st.write(result)


if __name__ == '__main__':
    main()
