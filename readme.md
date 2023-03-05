# Irrigator's backend project
In form of a Django Rest Framework API, basically

## A vague sketch of entities of the idea this is built on
::: mermaid
  classDiagram
    
    User "1" -- "*" Estate
    Estate "1" -- "*" WaterSupply
    WaterSupply "1" -- "*" FieldPlantation
    FieldPlantation "1" -- "*" Schedule

    class User {
      props...
    }
    
    note for Estate "The real estate property where plantation fields are"
    class Estate {
      props...
    }

    note for WaterSupply "From where a field gets its water to irrigate itself"
    class WaterSupply {
      props...
    }

    class FieldPlantation {
      props...
    }

    note for Schedule "When does a field irrigate"
    class Schedule {
      props...
    }
:::