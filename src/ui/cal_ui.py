from services.cal_service import cal_service
class UI:
    def __init__(self):
        """
        Constructor that creates the calculator UI/buttons.
        """
        self.create_buttons()
        
    def create_buttons(self):
        """
        Generates all the calculator buttons.
        """
        cal_service.numerical_values()
        cal_service.equals_btn()
        cal_service.plus_btn()
        cal_service.minus_btn()
        cal_service.multiplication_btn()
        cal_service.division_btn()
        cal_service.percent_btn()
        cal_service.plusminus_btn()
        cal_service.ac_btn()
        cal_service.sqrt_btn()
        cal_service.del_btn()
        cal_service.sqrd_btn()
        cal_service.reci_btn()
        cal_service.facto_btn()

    def start(self):
        """
        Iniates components and starts the UI 
        """
        cal_service.root.mainloop()      