pub fn square_fill(n: u8) {
    for _ in 0..=n {
        for _ in 0..=n {
            print!("* ");
        }
        println!();
    }
}
