import json
import re

def clean_and_parse_exam_data(txt_path, json_path):
    database = {}
    current_year = "未知年度"
    
    with open(txt_path, 'r', encoding='utf-8') as f:
        raw_lines = [line.strip() for line in f if line.strip()]
        
    print("開始進行過濾...")
    
    processed_lines = []
    temp_line = ""
    
    for line in raw_lines:
        if line.startswith("[YEAR=") and line.endswith("]"):
            if temp_line: processed_lines.append(temp_line)
            processed_lines.append(line)
            temp_line = ""
            continue
            
        if any(keyword in line for keyword in ["最低錄取標準", "錄取人數", "代碼 校名", "普通生", "原住民", "退伍軍人", "系組"]):
            continue
            
        if re.match(r'^\d{4}\s', line):
            if temp_line: processed_lines.append(temp_line)
            temp_line = line
        else:
            if temp_line: temp_line += " " + line
            else: temp_line = line
                
    if temp_line: processed_lines.append(temp_line)

    subject_keywords = ["國", "英", "數", "物", "化", "生", "歷", "地", "公", "社", "自", "聽"]

    for line_info in processed_lines:
        if line_info.startswith("[YEAR="):
            current_year = line_info.replace("[YEAR=", "").replace("]", "")
            continue
            
        parts = line_info.split()
        if len(parts) < 7:
            continue
            
        try:
            code = parts[0]
            school_name = parts[1]
            major_name = parts[2]
            full_title = f"{school_name} {major_name}"
            
            formula_parts = []
            next_idx = 3
            while next_idx < len(parts) and 'x' in parts[next_idx]:
                formula_parts.append(parts[next_idx])
                next_idx += 1
                
            formula_str = " ".join(formula_parts)
            
            quota = parts[next_idx]
            min_score = float(parts[next_idx + 1])
            
            remark_parts = []
            start_check_idx = next_idx + 2 
            
            for idx in range(start_check_idx, len(parts)):
                p = parts[idx]
                
                if "-----" in p:
                    break
                
                if re.match(r'^\d+(\.\d+)?$', p):
                    prev_p = parts[idx - 1]
                    is_prev_subject = any(sub in prev_p for sub in subject_keywords)
                    
                    if is_prev_subject:
                        remark_parts.append(p)
                    else:
                        break
                else:
                    remark_parts.append(p)
                
            filter_note = "----" if not remark_parts else " ".join(remark_parts)
            

            subjects = re.findall(r'([^\dx\s]+)x([\d\.]+)', formula_str)
            weights_dict = {}
            for sub, weight in subjects:
                weights_dict[sub] = float(weight)
                
            if code not in database:
                database[code] = {
                    "name": full_title,
                    "history": {}
                }
                
            database[code]["history"][current_year] = {
                "min_score": min_score,
                "full_formula": formula_str,
                "weights": weights_dict,
                "filter": filter_note
            }
            
        except Exception as e:
            continue

    with open(json_path, 'w', encoding='utf-8') as jf:
        json.dump(database, jf, ensure_ascii=False, indent=2)
        
    print(f"完成!")

clean_and_parse_exam_data('source.txt', 'data.json')
