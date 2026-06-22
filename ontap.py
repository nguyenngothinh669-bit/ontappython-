class Store:
    def __init__(self,store_id,name,revenue_day,open_days,bonus):
        self.id = store_id 
        self.name = name 
        self.revenue_day = revenue_day
        self.open_days = open_days
        self.bonus = bonus 
        self.net_revenue = 0.0 
        self.performance_type = "" 
        
        self.calculate_net_revenue()
        self.classify_performance() 
        
    def calculate_net_revenue(self):
        self.net_revenue = (self.revenue_day * self.open_days) + self.bonus 
        
    def classify_performance(self): 
        if self.net_revenue < 9000000:
            self.performance_type = "Thấp"
        elif 9000000 <= self.net_revenue <= 15000000:
            self.performance_type = "Trung bình"
        elif 15000000 <= self.net_revenue <= 30000000:
            self.performance_type = "Khá"
        else: 
            self.performance_type = "Cao" 
            
                
class StoreManager:
    def __init__(self): 
        self.stores = []
        self._load_sample_data() 
        
    def _input_string(self,prompt,check_empty= True): 
        while True: 
            val = input(prompt).strip()
            if check_empty and not val: 
                print("Lỗi: Bắt buộc phải không được để trống!")
            else: 
                return val 
            
    def _input_positive_number(self,prompt,is_float = True) : 
        while True: 
            try: 
                val_str = input(prompt).strip()
                if not val_str : 
                    print("Lỗi: Bắt buộc phải không được để trống!")
                    continue 
                val = float(val_str) if is_float else int(val_str) 
                if val < 0 : 
                    print("Lỗi: Giá tiền không được âm phải lớn hơn >=0")
                else: 
                    return val 
            except ValueError: 
                print("Lỗi: Vui lòng nhập đúng định dạng") 
                
    def _input_open_days(self) : 
        while True: 
            days = self._input_positive_number("Nhập số ngày mở cửa (0-31): ") 
            if 0 <= days <= 31:
                return days 
            print("Lỗi: Số ngày mở của phải nằm trong từ 0 đến 31")
            
    def _find_store_index_by_id (self,store_id): 
        for i , store in enumerate(self.stores): 
            if store.id == store_id.upper(): 
                return i 
        return -1 
    
    
    def add_store(self): 
        print("\n--- THÊM CỦA HÀNG MỚI ---")
        while True: 
            store_id = self._input_string("Nhập mã cửa hàng: ") 
            if self._find_store_index_by_id(store_id) != -1: 
                print(f"Lỗi: Mã cửa hàng '{store_id.upper()}' đã tồn tại trong hệ thống.Vui lòng nhập mẫ khác!")
            else: 
                break 
            
        name = self._input_string("Nhập tên của hàng: ")
        revenue_day = self._input_positive_number("Nhập doanh thu mục tiêu trong 1 ngày (VNĐ): ")
        open_days = self._input_open_days() 
        bonus = self._input_positive_number("Nhập doanh thu thưởng thêm (VNĐ): ") 
        
        new_store = Store(store_id.upper(), name.capitalize() , revenue_day, open_days,bonus) 
        self.stores.append(new_store) 
        print("\n Thêm của hàng thành công! Hệ thống tự động tính toán doanh thu và hiệu năng.") 
        
    def show_all(self): 
        print("\n--- Danh sách của hàng ---") 
        if not self.stores: 
            print("Danh sách hiện đang trống!")
            return 
        
        header = f"| {'Mã CH':<8} | {'Tên Cửa Hàng':<25} | {'DT Ngày':<15} | {'Ngày Mở':<8} | {'Thưởng':<15} | {'DT Thuần':<20} | {'Hiệu Năng':<15} |"
        print("-" * len(header)) 
        print(header) 
        print("-"*len(header)) 
        
        for s in self.stores: 
            print(f"| {s.id:<8} | {s.name:<25} | {s.revenue_day:<15,.0f} | {s.open_days:<8,.0f} | {s.bonus:<15,.0f} | {s.net_revenue:<20,.0f} | {s.performance_type:<15} |") 
        print("-"*len(header))  
    
    def update_store(self): 
        print("\n--- CẬP NHẬT THÔNG TIN CỬA HÀNG ---")
        if not self.stores: 
            print("Danh sách hiện đang trống, không thể cập nhật!")
            return 
        store_id = self._input_string("Nhập mã cửa hàng cần cập nhật: ")
        index = self._find_store_index_by_id(store_id) 
        
        if index == -1 : 
            print("Lỗi: Không tìm thấy mã này trong cửa hàng này") 
            return 
        print(f"Đang cập nhật cho cửa hàng: {self.stores[index].name}") 
        self.stores[index].revenue_day = self._input_positive_number("Nhập mới doanh thu trong 1 ngày: ")
        self.stores[index].open_days = self._input_open_days() 
        self.stores[index].bonus = self._input_positive_number("Nhập mới thưởng: ")
        
        self.stores[index].calculate_net_revenue() 
        self.stores[index].classify_performance() 
        print("\n Cập nhật thành công thông tin mới vàp cửa hàng")
    
    def delete_store(self): 
        print("\n--- XÓA CỪA HÀNG ---")
        if not self.stores: 
            print("Danh sách hiện đang trống, không thể xóa!")
            return  
        
        store_id = self._input_string("Nhập mã cửa hàng muốn xóa: ") 
        index = self._find_store_index_by_id(store_id) 
        
        if index == -1 : 
            print("Lỗi: Không tìm thấy mã này trong cửa hàng này") 
            return 
        
        confirm = input("Bạn có chắc muốn xóa cửa hàng này không? (Y): ").strip().upper()
        if confirm == "Y": 
            del self.stores[index]
            print("Đã xóa thành công cửa hàng này!")
        else: 
            print("Đã hủy thao tác") 
            
    def search_store(self): 
        print("\n--- Tìm kiếm cửa hàng ---")
        if not self.stores: 
            print("Danh sách hiện đang trống, không thể tìm kiếm!")
            return  
        keyword = self._input_string("Nhập từ khóa muốn tìm kiếm: ").lower() 
        found_stores = [s for s in self.stores if keyword in s.name.lower()] 
        
        if not found_stores: 
            print("Không tìm thấy cửa hàng phù hợp.")
        else: 
            print(f"\n Tìm thấy {len(found_stores)} kết quả:") 
            header = f"| {'Mã CH':<8} | {'Tên Cửa Hàng':<25} | {'DT Ngày':<15} | {'Ngày Mở':<8} | {'Thưởng':<15} | {'DT Thuần':<20} | {'Hiệu Năng':<15} |"
            print("-" * len(header)) 
            print(header) 
            print("-"*len(header)) 
            
            for s in found_stores: 
                print(f"| {s.id:<8} | {s.name:<25} | {s.revenue_day:<15,.0f} | {s.open_days:<8,.0f} | {s.bonus:<15,.0f} | {s.net_revenue:<20,.0f} | {s.performance_type:<15} |") 
            print("-"*len(header))  
    def statistics(self): 
        print("\n--- DANH SÁCH THỐNG KÊ HIỆU NĂNG ---")
        if not self.stores: 
            print(" Danh sách trống!")
            return 
        stats = {"Thấp": 0, "Trung bình": 0, "Khá": 0,"Cao": 0}
        for store in self.stores: 
            
    def _load_sample_data(self): 
        self.stores.append(Store("CH01", "Cửa hàng Quận 1", 300000, 5, 1000000)) 
        self.stores.append(Store("CH02", "Đại lý Tân Bình", 400000, 30, 2000000)) 
        self.stores.append(Store("CH03", "Cửa hàng Quận 7", 800000, 28, 5000000)) 
        self.stores.append(Store("CH04", "Flagship Thủ Đức", 1200000, 31, 8000000)) 
        
        
def main(): 
    manager = StoreManager() 
    
    while True: 
        print("\n================ MENU ================")
        print("1. Hiển thị danh sách cửa hàng")
        print("2. Thêm cửa hàng mới")
        print("3. Cập nhật thông tin cửa hàng")
        print("4. Xóa cửa hàng")
        print("5. Tìm kiếm cửa hàng")
        print("6. Thống kê hiệu năng")
        print("7. Thoát")
        print("========================================") 
        
        choice = input("Nhập lựa chọn của bạn (1-7): ").strip()
        
        if not choice: 
            print("Lựa chọn chức năng không được để trống!")
            continue 
        
        match choice: 
            case '1': 
                manager.show_all() 
            case '2': 
                manager.add_store() 
            case '3': 
                manager.update_store() 
            case '4': 
                manager.delete_store() 
            case '5': 
                manager.search_store() 
            case '7': 
                print("\nCảm ơn bạn đã sử dụng hệ thống quản lý cửa hàng & doanh thu!")
                break
            case _: 
                print("Lỗi: Lựa chọn không hợp lệ, vui lòng nhập từ 1 - 7") 
                
if __name__ == "__main__": 
    main()                                                                                         