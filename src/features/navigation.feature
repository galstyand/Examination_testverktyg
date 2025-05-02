#Som användare vill jag att knappen för den aktiva sidan i menyn ska ha en avvikande stil, så att jag tydligt kan se vilken sida jag befinner mig på.

  Feature: Aktiv knapp blir grå
    Scenario Outline: Navigera till sektion och markera som aktiv
      Given Användaren navigerar till Läslistan
      When Användaren navigerar till "<sektion>" som har testId: "<testid>"
      Then blir knappen med testId: "<testid>" inaktiv

      Examples:
     | sektion             | testid       |
     | Katalog             | catalog      |
     | Lägg till bok       | add-book     |
     | Mina böcker         | favorites    |