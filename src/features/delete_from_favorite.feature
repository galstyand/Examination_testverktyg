#Som användare vill jag kunna ta bort en bok från favoritlistan så att jag kan hålla listan uppdaterad.

  Feature: Ta bort en favoritmarkerad bok
    Scenario: Ta bort en favoritmarkerad bok
      Given Användaren står i Katalog
      When Användaren klickar på stjärnan på boken med titel "Min katt är min chef"
      And Användaren klickar på stjärnan på boken med titel "Min katt är min chef"
      And användaren navigerar till Mina Böcker
      Then ska "När du valt, kommer dina favoritböcker att visas här." texten visas

    Scenario: Favoritmarkera två böcker och ta bort den ena
      Given Användaren står i Katalog
      When Användaren klickar på stjärnan på boken med titel "Min katt är min chef"
      And Användaren klickar på stjärnan på boken med titel "Jag trodde det var tisdag"
      And Användaren klickar på stjärnan på boken med titel "Min katt är min chef"
      And användaren navigerar till Mina Böcker
      Then boken med titel "Jag trodde det var tisdag" är i listan