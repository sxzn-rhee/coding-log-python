from datetime import date 

def main(): 
    transactions = [
        {"date": "2026=01-10", "desc": "스타벅스", "amount": -5600, "category": "식비"},
        {"date": "2026-01-10", "desc": "급여", "amount": 2500000, "category": "수입"},
        {"date": "2026-01-11", "desc": "지하철",   "amount": -1400, "category": "교통"},
        {"date": "2026-01-11", "desc": "쿠팡",     "amount": -32900, "category": "쇼핑"},
        {"date": "2026-01-12", "desc": "편의점",   "amount": -4200, "category": "식비"},
    ]

    income = 0 
    expense = 0
    by_category = {} 

    for t in transactions:
        amt = t["amount"]
        cat = t["category"]

        if amt >= 0: 
            income += amt 
        else: 
            expense += -amt  # 지출은 양수로 합산
        
        by_category[cat] = by_category.get(cat, 0) + (amt if amt < 0 else 0)
                                                    
    print(f"=== Ledger Summary ({date.today()}) ===")
    print(f"수입 합계: {income:,}원")
    print(f"지출 합계: {expense:,}원")
    print(f"순이익: {income - expense:,}원")
    print("\n[카테고리별 지출]")
    for cat, amt in by_category.items():
        if amt < 0:
            print(f"- {cat}: {-amt:,}원")

if __name__ == "__main__":
    main()