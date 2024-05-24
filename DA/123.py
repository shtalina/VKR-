    def pentagon():
    #Тут уже пентагон
        cognitive_data = {
            "Познание": data.metric1,
            "Понимание": data.metric2,
            "Восприятие": data.metric3,
            "Представление": data.metric4,
            "Объяснение": data.metric5,
        }

        # Убедитесь, что у вас есть ровно 5 категорий и значений
        categories = list(cognitive_data.keys())

        # Получение списка значений для каждой категории
        values = list(cognitive_data.values())

        # Создаем фигуру для пентагонального графика
        fig = go.Figure()

        # Добавляем границы пентагона
        fig.add_trace(go.Scatterpolar(
            r=values + values[:1],
            theta=categories + categories[:1],
            fill='toself',
            name='Cognitive Metrics',
            line=dict(color='rgb(118, 138, 204)'),


        ))