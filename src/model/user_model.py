class User:
    
    def __init__(self, name: str, last_name: str, email: str, age: int) -> None:
        self.name = name
        self.last_name = last_name
        self.email = email
        self.age = age 

        
    def __repr__(self) -> dict:
        return {
            'nome': self.name,
            'sobrenome': self.last_name,
            'email': self.email,
            'idade': self.age
        }