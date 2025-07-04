import re
import math
import random
from datetime import datetime

class SmartMathChatbot:
    def __init__(self):
        self.name = "MathBot"
        self.memory = []
        self.operators = {'+': lambda x,y: x+y, '-': lambda x,y: x-y, '*': lambda x,y: x*y, '/': lambda x,y: x/y, '**': lambda x,y: x**y}
        
    def evaluate_expression(self, expr):
        try:
            # Safe evaluation of mathematical expressions
            allowed_chars = set('0123456789+-*/.() ')
            if all(c in allowed_chars for c in expr.replace('**', '*').replace('sin', '').replace('cos', '').replace('tan', '').replace('log', '').replace('sqrt', '')):
                expr = expr.replace('sin', 'math.sin').replace('cos', 'math.cos').replace('tan', 'math.tan')
                expr = expr.replace('log', 'math.log').replace('sqrt', 'math.sqrt').replace('pi', 'math.pi')
                return eval(expr)
            return None
        except:
            return None
    
    def solve_equation(self, equation):
        # Simple linear equation solver (ax + b = c)
        try:
            if '=' in equation:
                left, right = equation.split('=')
                left, right = left.strip(), right.strip()
                # Handle simple cases like "2x + 3 = 7"
                if 'x' in left and right.replace('.','').replace('-','').isdigit():
                    # Extract coefficients
                    parts = left.replace('-', '+-').split('+')
                    a, b = 0, 0
                    for part in parts:
                        if 'x' in part:
                            coeff = part.replace('x', '').strip()
                            a = float(coeff) if coeff and coeff != '-' else (1 if coeff != '-' else -1)
                        else:
                            b += float(part) if part.strip() else 0
                    c = float(right)
                    if a != 0:
                        return f"x = {(c - b) / a}"
            return "Cannot solve this equation type"
        except:
            return "Invalid equation format"
    
    def factorial(self, n):
        return math.factorial(int(n)) if n >= 0 else "Factorial not defined for negative numbers"
    
    def prime_check(self, n):
        n = int(n)
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True
    
    def fibonacci(self, n):
        n = int(n)
        if n <= 1: return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    def quadratic_formula(self, a, b, c):
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            return "No real solutions (complex solutions exist)"
        elif discriminant == 0:
            return f"One solution: x = {-b / (2*a)}"
        else:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            return f"Two solutions: x1 = {x1}, x2 = {x2}"
    
    def statistics(self, numbers):
        try:
            nums = [float(x) for x in numbers.split(',')]
            mean = sum(nums) / len(nums)
            nums.sort()
            median = nums[len(nums)//2] if len(nums)%2==1 else (nums[len(nums)//2-1] + nums[len(nums)//2])/2
            variance = sum((x - mean)**2 for x in nums) / len(nums)
            std_dev = math.sqrt(variance)
            return f"Mean: {mean:.2f}, Median: {median:.2f}, Std Dev: {std_dev:.2f}"
        except:
            return "Invalid number format. Use comma-separated values."
    
    def process_input(self, user_input):
        user_input = user_input.lower().strip()
        
        # Math expression evaluation
        if any(op in user_input for op in ['+', '-', '*', '/', '**', 'sin', 'cos', 'tan', 'log', 'sqrt']):
            result = self.evaluate_expression(user_input)
            if result is not None:
                return f"Result: {result}"
        
        # Equation solving
        if '=' in user_input and 'x' in user_input:
            return self.solve_equation(user_input)
        
        # Factorial
        if 'factorial' in user_input or '!' in user_input:
            nums = re.findall(r'\d+', user_input)
            if nums:
                return f"Factorial of {nums[0]}: {self.factorial(int(nums[0]))}"
        
        # Prime check
        if 'prime' in user_input:
            nums = re.findall(r'\d+', user_input)
            if nums:
                n = int(nums[0])
                return f"{n} is {'prime' if self.prime_check(n) else 'not prime'}"
        
        # Fibonacci
        if 'fibonacci' in user_input:
            nums = re.findall(r'\d+', user_input)
            if nums:
                return f"Fibonacci({nums[0]}): {self.fibonacci(int(nums[0]))}"
        
        # Quadratic formula
        if 'quadratic' in user_input:
            nums = re.findall(r'-?\d+\.?\d*', user_input)
            if len(nums) >= 3:
                a, b, c = float(nums[0]), float(nums[1]), float(nums[2])
                return f"Quadratic equation {a}x² + {b}x + {c} = 0:\n{self.quadratic_formula(a, b, c)}"
        
        # Statistics
        if 'statistics' in user_input or 'stats' in user_input:
            numbers = re.findall(r'-?\d+\.?\d*', user_input)
            if numbers:
                return self.statistics(','.join(numbers))
        
        # General responses
        greetings = ['hello', 'hi', 'hey', 'greetings']
        if any(word in user_input for word in greetings):
            return f"Hello! I'm {self.name}, your mathematical assistant. I can solve equations, calculate expressions, find factorials, check primes, and much more!"
        
        if 'help' in user_input:
            return """I can help you with:
• Basic math: 2+2, 3*4, 10/2, 2**3
• Trigonometry: sin(90), cos(0), tan(45)
• Equations: 2x + 3 = 7
• Factorials: factorial 5 or 5!
• Prime check: is 17 prime?
• Fibonacci: fibonacci 10
• Quadratic: quadratic 1 -5 6
• Statistics: stats 1,2,3,4,5
• And much more!"""
        
        return "I'm not sure how to help with that. Try asking about math problems, or type 'help' for examples!"
    
    def chat(self):
        print(f"🤖 {self.name} - Smart Mathematical Chatbot")
        print("=" * 50)
        print("Hello! I'm your AI mathematical assistant. Type 'quit' to exit.")
        print("Try: '2+2', 'solve 2x+3=7', 'factorial 5', 'is 17 prime?', 'help'")
        print("=" * 50)
        
        while True:
            try:
                user_input = input("\n💭 You: ")
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print(f"🤖 {self.name}: Goodbye! Happy calculating! 🧮")
                    break
                
                self.memory.append(f"User: {user_input}")
                response = self.process_input(user_input)
                self.memory.append(f"Bot: {response}")
                
                print(f"🤖 {self.name}: {response}")
                
            except KeyboardInterrupt:
                print(f"\n🤖 {self.name}: Goodbye! 👋")
                break
            except Exception as e:
                print(f"🤖 {self.name}: Sorry, I encountered an error. Please try again!")

# Run the chatbot
if __name__ == "__main__":
    bot = SmartMathChatbot()
    bot.chat()