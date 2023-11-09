import cv2
#Function to process images

def process_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale image", gray)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Video", frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
    

if __name__ == "__main__":
    choice = input("Enter i for image or v for video: ")
    if choice.lower() == 'i':
        image = cv2.imread('imgs&vids/community.jpg')
        process_image(image)
        
    elif choice.lower() == 'v':
        video_path = 'imgs&vids/m2-res_240p.mp4'
        process_video(video_path)
        
    else:
        print("Invalid Choice. Please enter i or v")