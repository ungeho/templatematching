import cv2

def main():
    # 検索対象の画像と検索したい画像の読み込み
    img = cv2.imread('taishou.png') # 検索対象の画像
    template = cv2.imread('sushi.png') #検索したい画像

    # 検索したい画像の高さと幅を取得
    height, width, channnels = template.shape

    # 画像の検索
    result = cv2.matchTemplate(img, template, cv2.TM_CCORR_NORMED)

    # マッチング操作を行った結果の類似度の最小値、最大値の画素とその位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)


    print("類似度の最小値               :" + str(min_val))
    print("類似度の最大値               :" + str(max_val))
    print("類似度最小値の座標（左上） 　：" + str(min_loc))
    print("類似度最大値の座標(左上) 　  :" + str(max_loc))
    print("検索したい画像の幅   　 　　 :" + str(width))
    print("検索したい画像の高さ 　  　　:" + str(height))

    # 検索結果（最大信頼度）の左上の座標を取得
    top_left = max_loc

    # 検索結果の右下の座標を取得?
    bottom_right = (top_left[0] + width, top_left[1] + height)

    # 検索対象画像内に、検索結果を長方形で描画
    # 第4引数はB,G,R、第5引数は線の太さ
    cv2.rectangle(img, top_left, bottom_right, color = (255, 255, 0), thickness = 2)

    #中心の座標を求める
    center = (int((top_left[0] + bottom_right[0])*0.5),int((top_left[1] + bottom_right[1])*0.5))

    # 検索結果の中心に水色の点を表示
    cv2.circle(img , center , radius = 1 , color = (255, 255, 0) , thickness = 2)


    # 一定の値kだけ高さを下げる（上下は下にいくほど数値が大きくなる）
    k = 110
    click_point = (int((top_left[0] + bottom_right[0])*0.5),int((top_left[1] + bottom_right[1])*0.5) + k)

    # クリックしたいポイントに赤色の点を表示
    cv2.circle(img , click_point , radius = 1 , color = (0, 0, 255) , thickness = 2)


    # 画像を保存
    cv2.imwrite('img.png',img)


if __name__ == "__main__":
    main()
