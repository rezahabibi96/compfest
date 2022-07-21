from orator.migrations import Migration


class CreateProductsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        if not self.schema.has_table('products'):
            with self.schema.create('products') as table:
                table.increments('id')
                table.string('name', 225)
                table.big_integer('price')
                table.text('desc')
                table.string('imagepath', 225)
                table.timestamp('timestamp')

    def down(self):
        """
        Revert the migrations.
        """
        pass
