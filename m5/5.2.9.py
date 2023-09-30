def uniq(st):
    st.replace(' ', '')
    return len(set(st))


print(uniq('        The Zen of Python'))
