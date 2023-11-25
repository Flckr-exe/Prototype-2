from tkinter import *
from PIL import ImageTk, Image
import cv2
from sample import *
from showPhotos import *
import customtkinter

customtkinter.set_appearance_mode("black")
customtkinter.set_default_color_theme("green")

class AttendaceApp:

    def __init__(self, window, title):
        self.window = window
        self.title = title
        window.title(self.title)
        window.geometry("500x500")
        window.iconbitmap("icon.ico")
        window.config(bg = "black")
        self.frame = customtkinter.CTkFrame(master=window)
        self.frame.pack(pady=20, padx=10, fill='both', expand=True)
        self.label = customtkinter.CTkLabel(master=self.frame, text="Smart Attendance System")
        self.label.pack(pady=12, padx=10)
        self.databutton = customtkinter.CTkButton(master=self.frame, text="Collect Sample", command=lambda:sampleDataWin())
        self.databutton.pack(pady=12, padx=10)
        self.showPhotos  = customtkinter.CTkButton(master=self.frame, text="Show Student Photos", command=lambda:showPhotosWin())
        self.showPhotos.pack(pady=12, padx=10)
        self.TrainData  = customtkinter.CTkButton(master=self.frame, text="Train Data", command=lambda:trainData())
        self.TrainData.pack(pady=12, padx=10)
        self.FaceRecog  = customtkinter.CTkButton(master=self.frame, text="Face Recognition", command=lambda:faceRecogniseWin())
        self.FaceRecog.pack(pady=12, padx=10)
           
def sampleDataWin():
    sample = Tk()
    at = SampleApp(sample, "Year 11")
    sample.mainloop()

def faceRecogniseWin():
    at = ShowPhotoApp(root, "Year 11")
    at.face_recog()

def showPhotosWin():
    showScreen = Tk()
    at = ShowPhotoApp(showScreen, "Year 11")
    at.show(showScreen, "Year 11")

def trainData():
    at = ShowPhotoApp(root, "Year 11")
    at.trainDataSample()


root = Tk()
at = AttendaceApp(root, "Year 11")
root.mainloop()