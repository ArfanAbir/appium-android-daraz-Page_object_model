from selenium.webdriver.common.by import By


class LoginLocators():
    first_next_buton_id = (By.XPATH, "//android.widget.TextView[@text='Bangladesh']")
    allow_button_id = (By.ID, 'android:id/button1')
    skip_button = (By.XPATH, "//android.widget.Button[@text='SKIP TO THE APP >']")
    account_icon = (By.XPATH, "//android.widget.TextView[@text='Account']")
    language_icon = (By.XPATH,"//android.widget.TextView[@resource-id='com.daraz.android:id/tv_settings']")
    language = (By.XPATH, "//android.widget.TextView[@text='ভাষা - Language']")
    bangla_language = (By.XPATH, "//android.widget.RadioButton[@text='বাংলা']")
    apply_btn = (By.XPATH, "//android.widget.Button[@text='APPLY']")
    search_bar = (By.ID, "com.daraz.android:id/laz_homepage_search_view")
    search_input = (By.ID, "com.daraz.android:id/search_input_box")
    search_btn = (By.ID, "com.daraz.android:id/search_button")
    filter_icon = (By.ID, "com.daraz.android:id/filter_image")
    acer_btn = (By.XPATH, "//android.widget.TextView[@text='Acer']")
    done_btn = (By.ID, "com.daraz.android:id/done_button")
    asus_btn = (By.XPATH,"//android.widget.TextView[@text='ASUS']")
    avita_btn = (By.XPATH, "//android.widget.TextView[@text='Avita']")
    basic_computer = (By.XPATH,"//android.widget.TextView[@text='Basic']")
    china_location = (By.XPATH, "//android.widget.TextView[@text='China']")
    darazmall_search = (By.XPATH, "//android.widget.TextView[@text='DarazMall']")
    dell_laptop = (By.XPATH, "//android.widget.TextView[@text='Dell']")
    category_arrow = (By.XPATH, "(//android.widget.TextView)[24]")
    gaming_laptop = (By.XPATH, "//android.widget.TextView[@text='Gaming Laptops']")
    list_view = (By.ID, "com.daraz.android:id/liststyle_icon")
    hp_laptop = (By.XPATH, "//android.widget.TextView[@text='HP']")
    lenovo_laptop = (By.XPATH, "//android.widget.TextView[@text='Lenovo']")
    msi_laptop = (By.XPATH, "//android.widget.TextView[@text='MSI']")
    login_signin = (By.XPATH, "//android.widget.TextView[@text='Login / Sign up']")
    login_with_password = (By.XPATH, "//android.widget.TextView[@text='Login with password']")
    mobile_email = (By.XPATH, "//android.widget.EditText[@text='Mobile Number/Email']")
    password = (By.XPATH, "//android.widget.EditText[@text='Password']")
    login_btn = (By.ID, "com.daraz.android:id/btn_next")
    traditional_laptop = (By.XPATH, "//android.widget.TextView[@text='Traditional Laptops']")

    min_price = (By.ID, "com.daraz.android:id/min_text")
    max_price = (By.ID, "com.daraz.android:id/max_text")







