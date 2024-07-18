# Airdrop Tool
Airdrop Tool là một script python giúp thực hiện tự động các tác vụ  của các kèo airdropthoong qua Api, hỗ trợ chạy trên mọi hệ điều hành như Android, Windows, MacOS...

##

**Nếu bạn gặp bất kì lỗi hay có thắc mắc nào trong quá trình sử dụng hãy đặt câu hỏi trong nhóm chat [@AirdropToolChat](https://.me/AirdropToolChat)**

### Tính năng
- Chạy tích hợp tất cả các kèo airdrop trong 1 script duy nhất
- Fake ip bằng proxy
- Fake User-agnet tự động
- Tự động cập nhật tool và bổ sung các tool mới
- Tự động chạy lại tool khi gặp lỗi giúp tool chạy liên tục mà không bị dừng

### Ưu điểm
- Tốn rất ít tài nguyên máy
- Có thể treo auto mà không cần mở máy (chỉ trên Android)

## HƯỚNG DẪN SỬ DỤNG
Khuyến khích mọi người sử dụng chrome hoặc các phần mềm antidetect browser trên máy tính để đăng nhập telegram vì dễ lấy data chạy tool mà không cần cài nhiều app như trên Android

Chạy tool trên máy tính có thể không giới hạn số luồng chạy tùy thuộc vào cấu hình máy nhưng phải treo máy liên tục, còn chạy tool trên Android chỉ có thể chạy tối đa 8 luồng đối với máy yếu mở max số luồng sẽ hơi nóng và lag nếu dùng thêm các tác vụ thông thường

### 1. CÀI ĐẶT CÁC ỨNG  CẦN THIẾT
#### TRÊN ĐIỆN THOẠI
Cài đặt các ứng dụng sau đây trên điện thoại để hỗ trợ chạy tool
- [Termux](https://play.google.com/store/apps/details?id=com.termux) dùng để chạy tool
- [RS duyệt tệp tin](https://play.google.com/store/apps/details?id=com.rs.explorer.filemanager&hl=vi) dùng để chỉnh sửa data chạy tool
- [VIA](https://play.google.com/store/apps/details?id=mark.via.gp) nên dùng để đăng nhập telegram trên điện thoại vì nó rất nhẹ so với các trình duyệt khác (nếu có máy tính thì nên đăng nhập trên máy tính)
- [BlackCanary](https://t.me/s/AirdropToolChannel/44) dùng để lấy data chạy tool trên điện thoại (nếu đăng nhập telegram trên máy tính thì bỏ qua app này)
- [AppCloner](https://t.me/s/AirdropToolChannel/43) dùng để nhân bản trình duyệt VIA trên điện thoại, tải nếu ae dùng nhièu acc telegram (nếu đăng nhập telegram trên máy tính thì bỏ qua app này)

#### TRÊN MÁY TÍNH
Cài đặt các phần mềm sau đây trên máy tính để hỗ trợ chạy tool
- [Python](https://www.python.org/downloads/) dùng để chạy tool
- [Git](https://gitforwindows.org/) dùng để cài các thư viện cần thiết


### 2. SETUP & TẢI TOOL
#### TRÊN ĐIỆN THOẠI
Mở ứng dụng **Termux** và chạy lần lượt các lệnh trong các ô dưới đây
```
termux-setup-storage
```
- Cho phép quyền đọc toàn bộ các tệp nếu được yêu cầu
```
pkg update && pkg upgrade && pkg install python && pkg install git && pip install requests && pip install termcolor && pip install brotli && pip install requests[socks] && pip install pystyle
```
- Nếu màn hình xuất hiện chữ `Continue? [Y/n]` thì nhấn enter, khi nào xuất hiện dấu `-$` là hoàn thành
```
cd /sdcard
```
```
rm -r /sdcard/airdroptool
```
```
git clone https://github.com/quangsangmmo/airdroptool/
```

#### TRÊN MÁY TÍNH
Mở ứng dụng **Cmd** và chạy lần lượt các lệnh trong các ô dưới đây
```
E:
```
```
rmdir /s /q airdroptool
```
```
git clone https://github.com/quangsangmmo/airdroptool/
```
### 3. LẤY DATA
#### TRÊN ĐIỆN THOẠI


#### TRÊN MÁY TÍNH
