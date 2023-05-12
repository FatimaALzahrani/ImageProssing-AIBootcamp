#OpenCV استيراد مكتبة 
import cv2

#image وتخزينها في متغير  img.jpg قراءة الصورة من ملف
image = cv2.imread("img.jpg")

#gray تحويل الصورة إلى الدرجات الرمادية وتخزينها في متغير 
gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

#"FatimaGray.jpg" حفظ الصورة الرمادية في ملف جديد بإسم 
cv2.imwrite("FatimaGray.jpg" , gray)

#FatimaGray عرض الصورة الرمادية على الشاشة فيي نافذه اسمها
cv2.imshow('FatimaGray',gray)

#F انتظار الضغط على أي مفتاح على لوحة المفاتيح وتخزين القيمة المرتبطة به في المتغير 
F = cv2.waitKey(0)


# في لوحة المفاتيح او 27 s إذا تم الضغط على مفتاح الـ 
if F == 27 or F == ord('s'):
#فإن جميع النوافذ المفتوحة في البرنامج ستتم إغلاقها
    cv2.destroyAllWindows()