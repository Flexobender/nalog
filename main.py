import streamlit as st
def outcome(t):
    if t<0:
        return 0
    else:
        return t
st.write(" Это приложение для расчета НДФЛ при продаже недвижимости")
def nalog():
    rate = 0.13
    tax = 0
    more5 = st.checkbox('Срок владения больше 5 лет',True,None,'Оставьте пустым если меньше')
    # сроки владения жильем
    if not more5:
        living = st.checkbox('Продажа жилого помещения', True, None, 'Оставьте пустым если продаете нежилое')
        more3 = st.checkbox('Срок владения больше 3 лет', False, None, 'Оставьте пустым если владеете меньше 3 лет')
        tax_resident = st.checkbox('Налоговый резидент', True, None, 'Находились в России 183 дня в налоговом году')
        if more3 & living:
            sole_home = st.checkbox('Продал единственное жилье', False, None, 'По общему правилу под единственным жильем понимается жилое помещение, которое является для гражданина и членов его семьи единственным пригодным для постоянного проживания')
            second_home_bought_in_90_days_before = st.checkbox('Купил второе жилье втечении 90 дней до регистрации продажи')
            privatisation = st.checkbox('Продажа приватизированного жилья')
            gift = st.checkbox('Жилье подарил близкий родственник или член семьи',False, None, 'Согласно ст. 2 СК РФ к членам семьи отнесены супруги, родители и дети, а также усыновители и усыновленные. А близкими родственниками считаются родственники по прямой восходящей и нисходящей линии: родители и дети, дедушка, бабушка и внуки, полнородные и неполнородные (имеющие общих отца или мать) братья и сестры (ст. 14 СК РФ)')
            renta = st.checkbox('Жилье получено по договору пожизненного содержания с иждивением')
            if sole_home | second_home_bought_in_90_days_before | privatisation | gift | renta:
                return outcome(tax)
        cost = 0
        cost_reduct = 0
        if tax_resident:
            no_cost = st.checkbox('Нет документов по расходам на приобретение')
            second_reduct = st.checkbox('Налоговый вычет уже использован в этом году')
            if living:
                cost_reduct = 1000000
            else:
                cost_reduct = 250000
            if not no_cost:
                cost = st.number_input('Сумма подтвержденных расходов')
            elif second_reduct:
                cost_reduct = 0
        else:
            rate = 0.3
        income = st.number_input('Сумма продажи в договоре')

        tax = (income - max(cost, cost_reduct)) * rate
    else:
        tax = 0
    return outcome(tax)
st.write('Ваш налог: ', nalog())


