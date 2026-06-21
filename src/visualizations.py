import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import os

class PortfolioVisualizer:
    """
    A class to create visualizations for portfolio analysis.
    """
    
    def __init__(self, portfolio_file, output_dir='output/charts'):
        """
        Initialize the visualizer.
        
        Args:
            portfolio_file (str): Path to CSV file with portfolio data
            output_dir (str): Directory to save charts
        """
        self.portfolio = pd.read_csv(portfolio_file)
        self.portfolio['current_price'] = pd.to_numeric(self.portfolio['current_price'])
        self.portfolio['purchase_price'] = pd.to_numeric(self.portfolio['purchase_price'])
        self.portfolio['quantity'] = pd.to_numeric(self.portfolio['quantity'])
        self.portfolio['current_value'] = self.portfolio['quantity'] * self.portfolio['current_price']
        self.portfolio['purchase_value'] = self.portfolio['quantity'] * self.portfolio['purchase_price']
        self.portfolio['gain_loss'] = self.portfolio['current_value'] - self.portfolio['purchase_value']
        self.portfolio['return_pct'] = (self.portfolio['gain_loss'] / self.portfolio['purchase_value']) * 100
        
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def plot_portfolio_allocation(self):
        """Create a pie chart of portfolio allocation."""
        fig = go.Figure(data=[go.Pie(
            labels=self.portfolio['symbol'],
            values=self.portfolio['current_value'],
            hole=0
        )])
        
        fig.update_layout(
            title="Portfolio Allocation by Current Value",
            font=dict(size=12),
            height=600
        )
        
        fig.write_html(f'{self.output_dir}/portfolio_allocation.html')
        print("✅ Portfolio allocation chart saved")
    
    def plot_returns_comparison(self):
        """Create a bar chart comparing returns for each stock."""
        fig = go.Figure(data=[
            go.Bar(
                x=self.portfolio['symbol'],
                y=self.portfolio['return_pct'],
                marker=dict(
                    color=self.portfolio['return_pct'],
                    colorscale='RdYlGn',
                    showscale=False
                )
            )
        ])
        
        fig.update_layout(
            title="Stock Return Percentage (%)",
            xaxis_title="Stock Symbol",
            yaxis_title="Return (%)",
            height=500,
            hovermode='x unified'
        )
        
        fig.write_html(f'{self.output_dir}/returns_comparison.html')
        print("✅ Returns comparison chart saved")
    
    def plot_gain_loss(self):
        """Create a bar chart showing gain/loss for each stock."""
        colors = ['green' if x > 0 else 'red' for x in self.portfolio['gain_loss']]
        
        fig = go.Figure(data=[
            go.Bar(
                x=self.portfolio['symbol'],
                y=self.portfolio['gain_loss'],
                marker=dict(color=colors)
            )
        ])
        
        fig.update_layout(
            title="Gain/Loss by Stock ($)",
            xaxis_title="Stock Symbol",
            yaxis_title="Gain/Loss ($)",
            height=500,
            hovermode='x unified'
        )
        
        fig.write_html(f'{self.output_dir}/gain_loss.html')
        print("✅ Gain/Loss chart saved")
    
    def plot_invested_vs_current(self):
        """Create a comparison chart of invested vs current value."""
        fig = go.Figure(data=[
            go.Bar(
                name='Invested Value',
                x=self.portfolio['symbol'],
                y=self.portfolio['purchase_value'],
                marker=dict(color='steelblue')
            ),
            go.Bar(
                name='Current Value',
                x=self.portfolio['symbol'],
                y=self.portfolio['current_value'],
                marker=dict(color='darkorange')
            )
        ])
        
        fig.update_layout(
            title="Invested vs Current Value by Stock",
            xaxis_title="Stock Symbol",
            yaxis_title="Value ($)",
            barmode='group',
            height=500,
            hovermode='x unified'
        )
        
        fig.write_html(f'{self.output_dir}/invested_vs_current.html')
        print("✅ Invested vs Current value chart saved")
    
    def generate_all_charts(self):
        """Generate all visualizations."""
        print("\n📊 Generating visualizations...")
        self.plot_portfolio_allocation()
        self.plot_returns_comparison()
        self.plot_gain_loss()
        self.plot_invested_vs_current()
        print(f"\n✅ All charts saved to {self.output_dir}/\n")


# Example usage
if __name__ == "__main__":
    visualizer = PortfolioVisualizer('data/portfolio.csv')
    visualizer.generate_all_charts()
