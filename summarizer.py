# -*- coding: utf-8 -*-

import gensim.models.keyedvectors as word2vec
import utils
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
import math

def summarize(content, n_clusters=0):
    w2v_model = word2vec.KeyedVectors.load('w2v.model')
    vocabulary = list(w2v_model.index_to_key)
    # print('\nContent\n', content)
    X, sentences = utils.preprocess(content, vocabulary, w2v_model, False)
    if n_clusters == 0:
        if len(sentences) > 25:
            n_clusters = math.ceil(len(sentences)/5)
        else:
            n_clusters = 5
    if len(sentences) < n_clusters:
        n_clusters = len(sentences)

    kmeans = KMeans(n_clusters=n_clusters)
    kmeans = kmeans.fit(X)

    print("K-Means Clustering\n")
    avg = []
    for j in range(n_clusters):
        print("Cụm", j + 1)
        idx = np.where(kmeans.labels_ == j)[0]
        print(idx)
        avg.append(np.mean(idx))
        print("Thứ tự trung bình: ", round(np.mean(idx), 2))
        print("=" * 100)
    closest, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_, X)
    print("Các câu gần", n_clusters, "tâm cụm nhất", closest)
    ordering = sorted(range(n_clusters), key=lambda k: avg[k])
    # print(ordering)
    print("\nKết quả tóm tắt:\n")
    # print(ordering)
    # summary = ' '.join([sentences[closest[idx]] for idx in ordering])
    print(len(sentences))
    # print('processed: ', summary)
    raw_sentences = utils.sent_tokenize(content)
    summary = ' '.join([raw_sentences[closest[idx]] for idx in ordering])
    # print(len(raw_sentences))
    print(summary)
    # print(content)
    return summary, n_clusters


# content = r'iPhone Pro 11 Max đang chạy hệ điều hành iOS 13 mới nhất của Apple. Về hiệu năng, iPhone 11 Pro Max là iPhone mạnh nhất hiện nay. Điểm Geekbench của iPhone 11 Pro Max là 3420, con số này thể hiện rằng 11 Pro Max mạnh hơn khoảng 10% so với iPhone 11 và hơn 20% so với iPhone XS Max. Nhưng đây chỉ là những con số, còn hiệu năng thực tế của iPhone 11 Pro Max khi sử dụng hàng ngày thì sao?. Thật khó để có thể khiến iPhone chậm đi, bởi vì máy có tốc độ khởi động ứng dụng rất nhanh và bạn có thể sử dụng chúng ngay lập tức. Tuy nhiên, camera là ứng dụng duy nhất iPhone thể hiện sự chậm chạp, phải mất một giây để tải ứng dụng (đôi khi nó có thể bị đứng). Khi bạn chụp ảnh bằng ống kính siêu rộng xem, hình ảnh cũng không xuất hiện ngay lập tức khi nhấn nút chụp. Tải ảnh để chỉnh sửa cũng mất một hoặc hai giây, cũng như một số thao tác lưu hình ảnh. Chúng tôi đánh giá cao việc iPhone có thể chịu được một lượng lớn hình ảnh được xử lý. Tuy nhiên, chúng tôi mong đợi mọi thứ sẽ nhanh hơn một chút, thay vì phải để xem một bánh xe quay quay trong quá trình xử lý. Thêm nữa, khi xem một bộ phim được tải về và tua đến một cảnh tùy ý thì iPhone lại bị đứng. Mỗi năm một lần, hội rước đèn đêm Trung thu ở xã em diễn ra tại sân vận động của xã rất từng bừng, náo nhiệt. Tối mười bốn tháng tám âm lịch, trên bãi sân rộng, thiếu nhi trong xã xếp hàng từng đội theo xóm. Tay bạn nào cũng cầm theo một cái lồng đèn được mua hoặc tự làm hay ống tre làm thành đuốc. Ban tổ chức gọi tổ trưởng lên bàn nhận bánh kẹo về cho tổ mình. Sau khi tổ trưởng phát xong kẹo bánh, có vài tiết mục văn nghệ “Cây nhà lá vườn” diễn ra ở sân rộng, thiếu niên nhi đồng vỗ tay theo nhịp, ủng hộ những nghệ sĩ không chuyên nghiệp của xã nhà. Tiếp đó là lệnh đốt nến. Tất cả các lồng đèn, đuốc được thắp sáng. Lúc bấy giờ sân bãi đẹp lung linh, kì ảo với hàng trăm ánh nến xanh, vàng, đỏ và ánh hồng của cây đuốc làm bằng ống tre. Lễ rước đèn Trung thu bắt đầu bằng bài hát “Rước đèn Trung thu”. Thiếu nhi vừa cầm lồng đèn, vừa hát “Tết Trung thu...”. Đoàn rước đèn đi một vòng quanh xã. Các cô chú Đội sản xuất và các anh chị Thanh niên xã đoàn đi kèm thiếu nhi đều giữ hàng ngũ ngay ngắn, trật tự, vừa tạo mĩ quan của hội rước đèn, vừa coi sóc phòng cháy (do đốt đèn nến và đuốc nên phải tăng cường phòng vệ, trông coi). Dọc đường, có bạn cầm lồng đèn từ trong nhà chạy ra nhập vào đoàn thiếu nhi đang “rồng rắn” rước đèn. Trên đường về, bạn nàonhà gần đường đi rước đèn có thể tách hàng về nhà. Trăng lúc này đã lên cao, tròn vành vạnh soi ánh vàng trong trẻo xuống mặt đất. Đoàn thiếu nhi vừa đi, vừa hát trở lại chỗ xuất phát. Các anh chị xã đoàn bắt nhịp bài hát "Như có Bác trong ngày đại thắng”. Kết thúc ngày hội, chúng em chia tay nhau và ra về. Buổi lễ rước đèn là sinh hoạt rất vui của thiếu nhi xã em và đã trở thành thông lệ không thể thiếu trong ngày lễ Trung Thu. Em rất yêu quê và yêu ngày hội Trung thu ở quê hương mình.'
# # content = r'iPhone Pro 11 Max đang chạy hệ điều hành iOS 13 mới nhất của Apple. Về hiệu năng, iPhone 11 Pro Max là iPhone mạnh nhất hiện nay. Điểm Geekbench của iPhone 11 Pro Max là 3420, con số này thể hiện rằng 11 Pro Max mạnh hơn khoảng 10% so với iPhone 11 và hơn 20% so với iPhone XS Max. Nhưng đây chỉ là những con số, còn hiệu năng thực tế của iPhone 11 Pro Max khi sử dụng hàng ngày thì sao?.'
# result = summarizer(content, 8)