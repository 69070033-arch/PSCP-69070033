"""3227: [LEARNING LOGS] ไพ่ 44 ใบ"""

card = input().lower()
txtdic = {
    "a":"ace",
    "j":"jack",
    "q":"queen",
    "k":"king",
}
shadedic = {
    "d":"diamonds",
    "h":"hearts",
    "s":"spades",
    "c":"clubs"
}

front_text = txtdic.get(card[:-1], card[:-1])
back_text = shadedic.get(card[-1], card[-1])
print(f"{front_text} of {back_text}")
