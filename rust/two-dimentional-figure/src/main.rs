#[path = "lib/square.rs"]
mod square;

fn print_square() {
    let side: u8 = 6;
    println!("Square {}", side);
    println!();
    square::square_fill(side);
    println!();
}

fn main() {
    println!("-------------------------------");
    print_square();
}
