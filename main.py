import tkinter as tk
from tkinter import ttk , messagebox
def __init__(self,root):
    self.root=root
    self.root.title('Restaurent Management System')
    self.menu_items={
        'Fries Meal':2,
        'Lunch Meal':2,
        'Burger Meal':3,
        'pizza Meal':4,
        'Chesse Burger':2.5,
        'Drinks ':1
    }
    self.exchange_currency=133
    self.setup_background(root)
    frame=ttk.Frame(root)
    frame.place(relx=0.5,rely=0.5,anchor=tk.center )

    ttk.label(frame,text='Restaurent order management',font=('Arieal',20,'bold')).grid(row=0,columnspan=3,padx=10,pady=10)
    self.menu_label={}
    self.menu_quantities={}
    for i,(items,price) in enumerate(self.self_menu.items(),start=1):
        label=ttk.Label(frame,
                        text=f'{items}(${price})',
                        font=('Arieal',12))
        label.grid(row=i,column=0,padx=10,pady=5)
        self.menu_labels[items]=label
        quantity_entry=ttk.Entry(frame,width=5)
        quantity_entry.grid(row=i,column=1,padx=10,pady=5)
        self.menu_quantites[items]=quantity_entry
        self.currency_var=tk.StringVar()
        ttk.Label(frame,text='Currency:',font=('Arieal',12)).grid(row=len(self.menu_items)+1,column=0,padx=10,pady=5)
        currency_dropdown=ttk.Combobox(frame,
                                       textvariable=self.currency_var,
                                       state='readonly',
                                       width=18,
                                       values=('USD','NPR'))
        currency_dropdown.currency(0)
        self.currency_var.trace('w',self.update_menu_prices)
        order_button=ttk.Button(frame,
                                text='Place Order'
                                command=self.place.order)
        order_button.grid(row=len(self.menu_items)+2,
                          columnspan=3,
                          padx=10,
                          pady=10)
def set_background(self,root):
    bg_width,bg_height=800,600
    canvas=tk.Canvas(root,widht=bg_width,height=bg_height)        
    canvas.pack()
    original_img=tk.PhotoImage(file='')
    background_img=original_img.subsample(
        original_img.width()//bg_width,
        original_img.height()//bg_height
    )
    canvas.create_image(0,0,anchor=tk.NW,image=background_img)
    canvas.image=background_img
def update_menu_prices(self,*args):
    currency=self.currency_var.get()
    symbol='₹' if currency=='NPR' else '$'
    rate=self.exchange_rate if currency=='NPR' else '1'
    for item,label in self.menu_labels.items():
        price=self.menu_label[item]*rate
        label.comfig(text=f"{item},({symbol}{price}):")
def place_order(self):
    total_cost=0
    order_summmary='Order Summary:\n'
    currency=self.currency_var.get()
    symbol='₹' if currency=='NPR' else '$'
    rate=self.exchange_rate if currency=='NPR' else 1
    for item,entry in self.menu_quantites.items():
        quantity=entry.get()
        if quantity.isdigit():
            quantity=int(quantity)
            price=self.menu_items[item]*rate
            cost=quantity+rate
            total_cost+=cost
            if quantity>0:
                order_summmary+=f"{item}: {quantity}x{symbol}"{price} = {symbol}{cost}\n"
    if total_cost > 0:
      order_summary += f"\nTotal Cost: {symbol}{total_cost}"
      messagebox.showinfo(
      "Order Placed",
       order_summary) # Show order summary in a message box
    else:
# Show error if no items are ordered
     messagebox.showerror("Error", "Please order at least one item.")
# Main block to run the app
if __name__ == "__main__":
root = tk.Tk()
app = RestaurantOrderManagement(root)
root.geometry("800x600") # Set the size of the window
root.mainloop()
    









