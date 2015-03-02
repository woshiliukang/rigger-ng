#coding=utf8
import re
import interface,utls.rg_var
class vars(interface.resource):
    """
    å®ä¹ç¯å¢åé:
    !R.vars:
        A: 1
        B: "hello"
    """


    def depend_check(self,context) :
        pass

    def _allow(self,context):
        return True
    def _before(self,context):
        items = self.__dict__

        for name , val in   items.items():
            if re.match(r'__.+__',name):
                continue
            name= name.upper()
            setattr(context,name,val)
        utls.rg_var.import_dict(items)

class echo(interface.resource) :
    """
        !R.echo :
            value : "${PRJ_ROOT}"
    """
    def _allow(self,context):
        return True
    def _before(self,context):
        pass
    def _config(self,context):
        v = utls.rg_var.value_of(self.value)
        print("[echo] %s :%s " %(self.value,v))

class assert_eq(interface.resource) :
    """
    !R.assert
        value  : "${APP_SYS}"
        expect : "test"
    """
    def _allow(self,context):
        return True
    def _config(self,context):
        self.assert_eq(context)
    def assert_eq(self,context):
        value  = utls.rg_var.value_of(self.value)
        expect = utls.rg_var.value_of(self.expect)
        if value != expect :
            raise interface.rigger_exception("value: %s , expect : %s " %(value,expect))
    def _start(self,context) :
        self.assert_eq(context)

