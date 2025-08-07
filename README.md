# x DAO

DAO (Data Access Object) logic made for XXX project

* ✅ SQLAlchemy DAO works well
* ✅ Redis DAO works well

❗️Я не використовую:
* CQRS: на даному етапі це буде перегрузкою і ми не маємо багато файлів.
по факту, зараз тільки один сервіс
* ports: знову ж таки, зараз дуже мало абстракцій і було б overkill робити 
все в вигляді ``application/common/ports/getaways/...``

(Адаптери є, але тому що вони не малі і є сенс їх винести)

в майбутньому, звичайно, все можна зробити в вигляді інтеракторів і порт-адаптерів


# Domain
* user entity
* user interface (for DAO in the future)

# Application
* user service (get, create etc.)

# Infrastructure
* dao: implementation of domain interfaces. SQLAlchemy & Redis approaches
* database: 
