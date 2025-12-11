import cv2  # openCVライブラリのインポート

# 色取得関数
def get_color(event, x, y, flags, param):
    img=param
    if event == cv2.EVENT_LBUTTONDOWN:
        b, g, r = img[y, x]
        print(f"座標({x}, {y}) 䛾色：色相={b}, 彩度={g}, 明度={r}")

# 画像の読み込み
img = cv2.imread("./shot_test.png")
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# ウィンドウを表示してコールバック登録
cv2.imshow("image", img)
cv2.setMouseCallback("image", get_color, param=hsv_img)
cv2.waitKey(0)