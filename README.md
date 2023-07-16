# Polyp_Segmentation
  Use Google colab for training and testing
  
  Environment setting
  
      !pip install torchstat
      !pip install thop
      !pip install streamlit
1. Training
   
    Download Pretrain_weight (hardnet68.pth): https://drive.google.com/file/d/1l0vh1ms9h0EJbof4vnV_Esj1C3Ad0n5a/view?usp=drive_link
  
    Download testing dataset: https://drive.google.com/file/d/1us5iOMWVh_4LAiACM-LQa73t1pLLPJ7l/view
     
    Download training dataset: https://drive.google.com/file/d/17sUo2dLcwgPdO_fD4ySiS_4BVzc3wvwA/view

    Change the weight path in hardnet_68.py (line 203)

    Change the --train_path (line 152) & --test_path (line 155) in Train.py
  
    Then, run the Train.py
  
3. Testing 

    Donwload the weight i trained: https://drive.google.com/file/d/1ZQiEaGVLFmoUvV2IupGkxBqNwucHElgi/view?usp=drive_link

    Change the --pth_path in Test.py (line 12)

    Change the data_path in Test.py (line 17)
  
    Then, run the Test.py and get the inference results in results/
  
5. Streamlit
   
    Run the code below in Google colab:
   
        !streamlit run Streamlit.py & npx localtunnel --port 8501

    Copy the IP in External URL and visit your url
   
   ![image](https://github.com/HuiNov14/Polyp_Segmentation/assets/137488321/424c1310-8966-47b1-a734-f8e35f870a5e)
    
    Paste the IP you copied above into the field and click the "Click to Submit" button, like this:
   
   ![image](https://github.com/HuiNov14/Polyp_Segmentation/assets/137488321/2c832d92-c09f-496a-a01a-1e117eee8fcb)

    Then, you can use the Streamlit app by uploading the PDF file from the testing dataset and see the result, like this:

   ![image](https://github.com/HuiNov14/Polyp_Segmentation/assets/137488321/9c89a21b-f473-4cb6-8f50-91d574b78977)





   
