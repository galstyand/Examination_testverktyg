#Som användare vill jag kunna markera en bok som "favorit" så att jag vet vilka böcker ska jag läsa.

  Feature: Markera en bok som favorit i listan
    Scenario: Markera boken med titeln "Min katt är min chef" som favorit
      Given Användaren står i Katalog
      When Användaren klickar på stjärnan på boken med titel "Min katt är min chef"
      When Användaren navigerar till Mina Böcker
      Then boken med titel "Min katt är min chef" är i listan