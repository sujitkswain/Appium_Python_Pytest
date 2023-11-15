# Appium_Python_Pytest
This is the project for Appium, Python, and Pytest. ctreport-selenium is used for reporting. Basically, it is a hybrid framework.POM and data-driven testing have been followed.

Follow the below steps to set up the environment for this project.

1. Install the Java Development Kit (JDK)
2. Set up Java Environment Variable Path (check java version by java -version)
    Note: Below two path need to set in the Environment Variables
    JAVA_HOME: C:\Program Files\Java\jdk1.8.0_112 (You have enter your path, this is just
    example)
    PATH: your-unique-entries;%JAVA_HOME%\bin (make sure that the longish your-unique-
    entries does not contain any other references to another Java installation folder
3. Download and install Android SDK here
4. Setup the ANDRIOD_HOME Path in the Environment Variables i.e. C:\Users\”User
Name”\AppData\Local\Android\Sdk
5. Install Node JS from here: Node JS download(check node js version by node --version)
6. Also install npm after installing Node JS (npm install -g npm) (check npm version by npm
--version)
7. Now we need to install Appium for Windows. Go here and download Appium for Windows.
8. Preparing Mobile Device For Automation With Appium
 Connect your Mobile Testing device via USB to PC. Enable Developer Mode on
Mobile Phone before automating the app.
 Steps to Enable Developer Mode/Options on Android Phone or Tablet:
    1. Open Settings, Tap on ‘About’ Option, Tap on ‘Software Information’, Tap On
    ‘More’.
    2. Tap on “Build number” 7 times to enable Developer options.
    3. Go back to Settings and make sure that the “Developer options” setting is there.
    4. Tap on Developer options and turn on the USB Debugging option from the menu
    on the next screen.
    
     Download and install USB Drivers for the Mobile Testing device on PC. (If the USB
    drivers is not present.)
     In adb terminal type ‘adb devices’
    Type cmd in search then type adb devices —&gt;below details will show
    
    List of devices attached
    TA93305G0L      device
    Note: This will display the list of devices connected to the system. 
9. Now Start the Appium Server
10. Add the desire capabilities.(https://appium.io/docs/en/writing-running-appium/caps/) and
Start the session
11. For finding the element in Mobile:
o By using Appium Inspector Session
o By using UiAutomatorViewer (to open UiAutomatorViewer go to Uses/”User
Name”/Appdata/Local/Andriod/Sdk/tools/bin )

12. Finding App Package and Activity:
We can find the App details using the Android Debugging Bridge (ADB) interface in
a Command Prompt (Windows) or Terminal (Linux/Mac).
    1. Firstly, connect your Android device or emulator to the PC/Mac and open the App whose
    details you want to inspect.
     
    2. Open a Command Prompt or Terminal window and use ‘adb devices ‘command to see the
    list of connected devices. A list of Android devices connected to the Computer is displayed
    along with their device IDs.
    3. Finally, type the below-given command to get the information about the currently open
    application.
    For Mac/Linux:
    adb shell dumpsys window | grep -E &#39;mCurrentFocus&#39;
    For Windows:
    adb shell dumpsys window | find &quot;mCurrentFocus&quot;
    Here, the part before the &#39;/&#39; character is the Package name and the part after that is the
    Activity name.
