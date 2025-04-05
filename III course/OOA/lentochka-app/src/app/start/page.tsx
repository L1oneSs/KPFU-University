import { Header } from "@/components/layout/header";
import StartpageContent from "./components/StartpageContent";
import { Footer } from "@/components/layout/footer";

export default function Start() {
  return (
    <main>
        <Header></Header>
        <StartpageContent></StartpageContent>
        <Footer></Footer>
    </main>
  );
}