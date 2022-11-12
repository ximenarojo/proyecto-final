#import streamlit as st
#import pandas as pd
#import numpy as np
#st.title('Titulo del proyecto')
#st.write('**Bienvenido**')
#n = st.slider('n',5,100,step=1)
#chart_data= pd.DataFrame(np.random.randn(n),columns=['data'])
#st.line_chart(chart_data)

import streamlit as st
import pandas as pd
import numpy as np
df = pd.DataFrame(
 np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
 columns=['lat', 'lon'])
