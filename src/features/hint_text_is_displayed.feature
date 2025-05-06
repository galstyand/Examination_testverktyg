#Som UX-designer vill jag att meddelandet 'När du valt, kommer dina favoritböcker att visas här.' ska visas när listan är tom, så att användaren ska förstå varför inga böcker visas

  Feature: Visa text om och bara om inga böcker är favoritmarkerade
    Scenario: Det finns inga favoritmarkerade böcker
      Given Användaren står i Katalog
      When Det finns inga böcker favoritmarkerade
      And användaren navigerar till Mina Böcker
      Then ska "När du valt, kommer dina favoritböcker att visas här." texten visas

    Scenario: Det finns favoritmarkerade böcker
      Given Användaren står i Katalog
      When användaren markerar en bok som favorit
      And användaren navigerar till Mina Böcker
      Then ska "När du valt, kommer dina favoritböcker att visas här." texten inte visas