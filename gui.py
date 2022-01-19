# -*- coding: utf-8 -*-
from threading import Thread
from tkinter import *
import summarizer
import re
import utils


def process():
    try:
        n_row = nrow.get()
    # print(n_row)
    except:
        n_row = 0

    if not n_row or type(n_row) is not int or n_row < 0:
        n_row = 0
    # print(n_row)
    content = input_txt.get("1.0", 'end-1c')

    if not content:
        return -1

    is_url = re.search(r'^(https?:\/\/)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)', content)

    if is_url:
        content = utils.crawl_content(is_url.group())
        # print('raw content',content)
        input_txt.insert(END, '\n\n' + content)
        # return

    output.delete("1.0", 'end-1c')
    # print(content)
    result, n_cluster = summarizer.summarize(content, n_row)
    nrow.set(n_cluster)
    output.insert("1.0", result)

    return 0

def delete():
    # global nrow
    input_txt.delete("1.0", 'end-1c')
    output.delete("1.0", 'end-1c')
    nrow.set(0)
    root.update()
    return 0

def tts():
    if output.get("1.0", 'end-1c'):
        utils.speak(output.get("1.0", 'end-1c'))

root = Tk()
root.wm_title('Text summarizer')
# root.config(background="#FFFFFF")
root.geometry('1130x775+30+10')
input_label = Label(root, text='Input: ', font=('Helvetica Neue', 12))
input_label.grid(row=0, column=0, columnspan=10, padx=5, sticky=NW)
input_txt = Text(root, heigh=24, width=123, wrap=WORD, spacing2=8, padx=5, pady=5, font=('Helvetica Neue', 12), bg='white')
input_txt.grid(row=1, column=0, columnspan=10, padx=5, pady=5, sticky=W)
nrow_label = Label(root, text='Số câu: ', font=('Helvetica Neue', 12))
nrow_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)
nrow = IntVar(root)
nrow_entry = Entry(root, textvariable=nrow, font=('Helvetica Neue', 12))
nrow_entry.grid(row=2, column=1, sticky=W)
process_button = Button(root, text='Tóm tắt', font=('Helvetica Neue', 12), width=15, command=lambda: Thread(target=process).start())
process_button.grid(row=2, column=2, sticky=W)
delete_button = Button(root, text='Xoá', font=('Helvetica Neue', 12), width=15, command=delete)
delete_button.grid(row=2, column=3, sticky=W)
output_label = Label(root, text='Output: ', font=('Helvetica Neue', 12))
output_label.grid(row=3, column=0, columnspan=10, padx=5, sticky=NW)
tts_button = Button(root, text='🔊', font=('Helvetica Neue', 12), command=lambda: Thread(target=tts).start())
tts_button.grid(row=3, column=1, sticky=W)
output = Text(root, heigh=12, width=123, wrap=WORD, spacing2=8, padx=5, pady=5, font=('Helvetica Neue', 12), bg='white')
output.grid(row=4, column=0, columnspan=10, padx=5, pady=5, sticky=W)

root.mainloop()

# s = r'Bộ Y tế tối 8/1 công bố 16.553 ca nhiễm, gồm 16.513 ca tại 62 tỉnh, thành; số ca tại Hải Phòng tăng cao, toàn thành phố ở "vùng đỏ"; 240 ca tử vong. Như vậy, 24 giờ qua số ca nhiễm cả nước tăng 259 so với hôm qua, trong đó 12.055 ca cộng đồng). Hà Nội tiếp tục dẫn đầu về số ca nhiễm trong ngày và vẫn ở mức cao (2.791 ca). Khánh Hòa, Hải Phòng, Bình Định đều vượt 700 ca. Trung bình số ca nhiễm mới trong nước ghi nhận trong 7 ngày qua là 16.263 ca/ngày. Đến nay Việt Nam đã ghi nhận 30 ca nhiễm Omicron, đều cách ly ngay sau khi nhập cảnh, gồm tại: Quảng Nam 14, TP HCM 11, Thanh Hóa 2, Hà Nội, Hải Dương, Hải Phòng đều một. Trong ngày ghi nhận 240 ca tử vong, trong đó lần đầu tiên số ca tử vong tại TP HCM dưới 20 (cụ thể 18 ca). Số tử vong ở các tỉnh khác: Đồng Nai 27 ca, An Giang 20, Tiền Giang và Vĩnh Long 15, Long An và Cà Mau 14, Hà Nội 13, Đồng Tháp 12, Sóc Trăng và Kiên Giang 11, Tây Ninh 9, Cần Thơ 8, Khánh Hòa và Bình Dương 7, Bến Tre 6, Bà Rịa - Vũng Tàu và Trà Vinh 5, Huế và Bình Thuận 4, Phú Yên, Hậu Giang, Bạc Liêu, Quảng Ninh, Bình Định mỗi nơi 2, Quảng Ngãi, Đăk Nông, Thái Nguyên, Đà Nẵng, Đăk Lăk mỗi nơi một. Trung bình số tử vong ghi nhận trong 7 ngày qua là 215 ca. Tổng số ca tử vong tại Việt Nam tính đến nay là 34.117 ca, chiếm tỷ lệ 1,8% so với tổng số ca nhiễm. Tổng số ca tử vong tại Việt Nam đứng thứ 26/224 quốc gia, vùng lãnh thổ, số ca tử vong trên một triệu dân thứ 130. So với châu Á, tổng số ca tử vong tại Việt Nam đứng thứ 6/49 quốc gia, vùng lãnh thổ (thứ 3 ASEAN), số tử vong trên một triệu dân xếp thứ 26 (thứ 5 ASEAN). Đợt dịch thứ 4, số ca nhiễm trong nước là 1.870.417, trong đó 1.485.221 ca đã được công bố khỏi bệnh.'
# s = r'Hàng nghìn công nhân ở một số nhà máy lớn phía Nam ngừng việc đòi tăng thưởng Tết làm gia tăng áp lực lên các doanh nghiệp sau một năm chật vật vì dịch. Hai hôm nay, toàn bộ nhà máy của Công ty TNHH Pouchen Việt Nam, đóng ở phường Hóa An (TP Biên Hòa, Đồng Nai) phải dừng sản xuất vì công nhân ngừng việc phản đối chính sách thưởng Tết vừa được công bố. Trong khi công nhân yêu cầu nhà máy phải thưởng bằng năm ngoái thì phía doanh nghiệp thông báo khó đáp ứng. Covid-19 khiến nhà máy Pouchen ngưng sản xuất gần 3 tháng, một số tháng cầm chừng. Năm 2021, kế hoạch sản xuất không hoàn thành, lợi nhuận giảm. Theo thỏa ước lao động tập thể đã thống nhất giữa doanh nghiệp và công đoàn, hàng năm nhà máy có thưởng Tết nhưng tùy thuộc vào hiệu quả kinh doanh. Năm nay, làm ăn không hiệu quả nên thưởng Tết, công nhân nhận thấp nhất một tháng lương, cao nhất 1,54 tháng, thấp hơn 30% so với trước khi Covid-19 xuất hiện. Tương tự trường hợp Pouchen, giữa tháng 12/2021, hàng trăm công nhân Công ty TNHH Freetrend A, đóng tại Khu chế xuất Linh Trung II, TP Thủ Đức (TP HCM) đã ngừng việc yêu cầu ban giám đốc tăng tiền thưởng Tết. Trước đó, khi chưa xuất hiện dịch, tiền thưởng Tết hàng năm của công nhân ở Freetrend A làm việc chưa đủ 3 năm là một tháng lương và tăng dần theo thâm niên, người cao nhất nhận 3 tháng. Năm 2021, công ty ngưng sản xuất hơn 3 tháng. Kế hoạch sản xuất không đạt nên doanh nghiệp giảm mức thưởng Tết, vẫn với cách tính cũ nhưng tiền thưởng sẽ giảm còn 60%. Nhà máy ra thông báo thưởng Tết chiều hôm trước, sáng hôm sau nhiều lao động ngừng việc phản đối. Trước phản ứng của công nhân, doanh nghiệp buộc phải nâng lên 75%. Mức thưởng mới được áp dụng cho tất cả nhà máy toàn tập đoàn với khoảng 40.000 lao động. Lý giải tâm lý ngừng việc yêu cầu tăng tiền thưởng Tết của công nhân, bà Trần Thị Thanh Hà, Trưởng ban Quan hệ lao động (Tổng liên đoàn lao động Việt Nam), cho rằng năm 2021 người lao động đối mặt nhiều khó khăn do việc làm, thu nhập giảm. Đa phần công nhân không có tích lũy nên đặt nhiều kỳ vọng vào tiền thưởng Tết để thêm một khoản chi tiêu. Ngoài ra, người lao động cho rằng dịch ở Việt Nam mới tác động mạnh vài tháng trong năm 2021. Những năm trước tình hình sản xuất của nhà máy rất tốt nên doanh nghiệp có tích lũy, bằng chứng liên tục mở rộng xưởng, tăng tuyển dụng... "Người lao động mong muốn các ông chủ trích một phần tiền tích lũy để chia sẻ với họ lúc khó khăn", bà Hà nói. Đặc biệt khi Việt Nam thuộc nhóm nước có tỷ lệ phủ vaccine cao nhất thế giới, các nhà máy gần như hoạt động bình thường trở lại. Điều này khiến công nhân tin rằng tình hình sản xuất, kinh doanh năm 2022 sẽ tốt lên, nên thưởng Tết phải cao để họ có động lực gắn bó lâu dài. Pháp luật về lao động hiện nay không bắt doanh nghiệp phải có thưởng Tết cho người lao động mà chỉ là khuyến khích khi hoạt động kinh doanh đạt hiệu quả, làm ăn có lãi. Theo bà Hà, câu chuyện của nhà máy Pouchen, Freetrend A sẽ được giải quyết dễ dàng hơn nếu các thông tin về sản xuất, kinh doanh, đặc biệt là lợi nhuận của doanh nghiệp được công khai, minh bạch. "Cán bộ công đoàn cần được cung cấp và nắm rõ thông tin về lợi nhuận của doanh nghiệp để đưa ra mức thưởng tốt nhất và làm cơ sở để thương lượng. Trường hợp nhà máy thua lỗ thực sự, công đoàn cũng có cơ sở để thuyết phục người lao động chia sẻ", bà Hà nói. Dưới góc nhìn của chuyên gia kinh tế, TS Lê Duy Bình, Giám đốc Economica Việt Nam, cho rằng trước mắt những cuộc ngừng việc của hàng nghìn công nhân với lý do tăng thưởng Tết sẽ khiến các doanh nghiệp cùng ngành nghề lo lắng. Sau thời gian chật vật vì dịch, chuỗi cung ứng đứt gãy, đơn hàng chậm trễ nay tình hình sản sản xuất đang dần phục hồi. Các đơn hàng dệt may, da giày đang quay trở lại với các nhà máy Việt Nam. Nếu các vụ ngừng việc không sớm được giải quyết mà lan rộng sẽ khiến các hợp đồng "quay đầu" sang các thị trường khác. Bởi theo ông Bình, quan hệ lao động hài hòa ổn định là một trong những yếu tố quan trọng thu hút đầu tư. Chiếu theo quy định hiện hành, thưởng Tết cao hay thấp phụ thuộc nhiều vào sự thương lượng giữa đôi bên. Về quy mô toàn công ty đó là thỏa ước lao động tập thể được chủ doanh nghiệp thương lượng với công đoàn. Đối với cá nhân được thể hiện trong hợp đồng lao động. Khi một cuộc ngừng việc xảy ra, cơ quan chức năng, chính quyền địa phương cần xem xét yếu tố này, nếu phù hợp với quy định pháp luật cần giải thích để người lao động hiểu rõ, đồng thuận. Theo TS Bình, trong bối cảnh Covid-19 gây ra rất nhiều khó khăn cho nền kinh tế, doanh nghiệp phải gồng gánh nhiều chi phí, đặc biệt vẫn duy trì được lương, thưởng, đóng bảo hiểm xã hội cho người lao động là điều rất đáng quý. Người lao động cần nhìn về những mặt tích cực đó mới có thể đồng hành với nhau lâu dài. Nhận định của Tổng liên đoàn lao động, năm nay "khó có thưởng cao đột biến như những năm trước". Mức thưởng bình quân Tết Nhâm Dần bằng 60-70% năm ngoái, đặc biệt khu vực phía Nam giảm mạnh do ảnh hưởng đợt bùng phát dịch thứ 4, nhà máy tạm đóng cửa, ngưng hoạt động nhiều tháng liền. Nhiều doanh nghiệp đến lúc này chưa xây dựng kế hoạch thưởng Tết cho người lao động.'


